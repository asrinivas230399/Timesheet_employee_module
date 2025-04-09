from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import logging
from role_based_access_control import RoleBasedAccessControl
from audit_trail import AuditTrail

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='access.log',
                    filemode='a')

# Initialize Role-Based Access Control
rbac = RoleBasedAccessControl()

# Define Pydantic models
class EncryptionRequest(BaseModel):
    data: str
    key: str
    role: str

class DecryptionRequest(BaseModel):
    encrypted_data: str
    key: str
    role: str

# Encryption endpoint
@app.post("/encrypt")
async def encrypt_data(request: EncryptionRequest):
    if not rbac.has_permission(request.role, 'encrypt'):
        AuditTrail.log_access(request.role, 'encrypt - denied')
        raise HTTPException(status_code=403, detail="Permission denied.")
    
    AuditTrail.log_access(request.role, 'encrypt')
    key_bytes = request.key.encode()
    data_bytes = request.data.encode()
    encrypted_data = encrypt(data_bytes, key_bytes)
    return {"encrypted_data": encrypted_data.hex()}

# Decryption endpoint
@app.post("/decrypt")
async def decrypt_data(request: DecryptionRequest):
    if not rbac.has_permission(request.role, 'decrypt'):
        AuditTrail.log_access(request.role, 'decrypt - denied')
        raise HTTPException(status_code=403, detail="Permission denied.")
    
    AuditTrail.log_access(request.role, 'decrypt')
    key_bytes = request.key.encode()
    encrypted_data_bytes = bytes.fromhex(request.encrypted_data)
    decrypted_data = decrypt(encrypted_data_bytes, key_bytes)
    return {"data": decrypted_data.decode()}