from fastapi import Header, HTTPException
from jose import jwt, JWTError
import os
import sys

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    print("ERROR: SECRET_KEY environment variable is required but not set!")
    print("Please set SECRET_KEY in your .env file with a secure random string.")
    sys.exit(1)

ALGORITHM = "HS256"

async def verify_admin(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Authentication required. Please login first."
        )
    
    token = authorization.replace("Bearer ", "")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role = payload.get("role")
        
        if role != "admin":
            raise HTTPException(
                status_code=403,
                detail="Admin access required. Please login as admin to perform this action."
            )
        
        return True
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token. Please login again."
        )
