from fastapi import Request, Response
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def audit_middleware(request: Request, call_next):
    # Log the request details
    logger.info(f"Request: {request.method} {request.url}")
    
    # Process the request
    response: Response = await call_next(request)
    
    # Log the response details
    logger.info(f"Response: {response.status_code}")
    
    return response