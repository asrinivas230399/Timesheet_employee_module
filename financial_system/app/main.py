from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from .database import SessionLocal, engine
from datetime import timedelta

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Financial System API", description="API for financial systems communication.", version="1.0.0")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(auth.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/transactions/", response_model=schemas.Transaction, summary="Create a new transaction", description="Create a new financial transaction.")
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db), current_user: dict = Depends(auth.get_current_active_user)):
    db_transaction = crud.create_transaction(db=db, transaction=transaction)
    return db_transaction

@app.get("/transactions/{transaction_id}", response_model=schemas.Transaction, summary="Get a transaction by ID", description="Retrieve a transaction's details by its ID.")
def read_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: dict = Depends(auth.get_current_active_user)):
    db_transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@app.get("/transactions/", response_model=list[schemas.Transaction], summary="List transactions", description="Retrieve a list of transactions with pagination support.")
def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: dict = Depends(auth.get_current_active_user)):
    transactions = crud.get_transactions(db, skip=skip, limit=limit)
    return transactions
