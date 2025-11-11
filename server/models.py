from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserModel(BaseModel):
    username: str
    role: str = "user"
    signed_in_at: Optional[datetime] = None

    class Config:
        json_encoders = {ObjectId: str}

class LoginRequest(BaseModel):
    username: str
    role: str = "user"

class CategoryModel(BaseModel):
    name: str
    description: str
    tags: List[str] = []

    class Config:
        json_encoders = {ObjectId: str}

class TagModel(BaseModel):
    name: str

    class Config:
        json_encoders = {ObjectId: str}

class BlogPostModel(BaseModel):
    title: str
    content: str
    author: str
    category: str
    tags: List[str] = []
    featured: bool = False
    image_url: Optional[str] = None
    views: int = 0
    likes: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_encoders = {ObjectId: str}

class BlogPostCreate(BaseModel):
    title: str
    content: str
    author: str
    category: str
    tags: List[str] = []
    featured: bool = False
    image_url: Optional[str] = None

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    featured: Optional[bool] = None
    image_url: Optional[str] = None

class SummarizeRequest(BaseModel):
    blog_id: str

class ChatRequest(BaseModel):
    query: str
    blog_id: Optional[str] = None
