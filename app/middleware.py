from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log request data
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        # Log response data
        logger.info(f"Response status: {response.status_code}")
        return response