from datetime import datetime, timedelta
from models import UserModel, LoginRequest
from database import get_collection
from jose import jwt
import os
import sys

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    print("ERROR: SECRET_KEY environment variable is required but not set!")
    print("Please set SECRET_KEY in your .env file with a secure random string.")
    sys.exit(1)

ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def instant_login(login_request: LoginRequest):
    users_collection = get_collection("users")
    
    user_data = {
        "username": login_request.username,
        "role": login_request.role,
        "signed_in_at": datetime.utcnow()
    }
    
    existing_user = users_collection.find_one({"username": login_request.username})
    
    if existing_user:
        users_collection.update_one(
            {"username": login_request.username},
            {"$set": {"role": login_request.role, "signed_in_at": datetime.utcnow()}}
        )
        existing_user["role"] = login_request.role
        existing_user["signed_in_at"] = datetime.utcnow()
        existing_user["_id"] = str(existing_user["_id"])
        user_response = existing_user
    else:
        result = users_collection.insert_one(user_data)
        user_data["_id"] = str(result.inserted_id)
        user_response = user_data
    
    access_token = create_access_token({
        "sub": user_response["username"],
        "role": user_response["role"]
    })
    
    user_response["access_token"] = access_token
    return user_response
