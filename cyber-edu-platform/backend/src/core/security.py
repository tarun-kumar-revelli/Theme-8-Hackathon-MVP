from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Security(oauth2_scheme)) -> str:
    # Here you would implement the logic to decode the token and retrieve the user
    # For now, we will just raise an exception for demonstration purposes
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return "current_user"  # Replace with actual user retrieval logic

def check_permissions(user: str, permission: str) -> bool:
    # Implement permission checking logic here
    # For demonstration, we will allow all permissions for the current user
    return True

def secure_endpoint(user: str, permission: str):
    if not check_permissions(user, permission):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return {"message": "Access granted"}