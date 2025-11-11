from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from database import get_collection
from models import (
    BlogPostCreate, BlogPostUpdate, CategoryModel, 
    TagModel, SummarizeRequest, ChatRequest
)
from ai import summarize_blog, chat_with_blog
from dependencies import verify_admin

router = APIRouter()

def serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

@router.get("/blogs")
async def get_blogs(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    tag: Optional[str] = None
):
    blogs_collection = get_collection("blog_posts")
    
    query = {}
    if category:
        query["category"] = category
    if tag:
        query["tags"] = tag
    
    skip = (page - 1) * limit
    
    blogs = list(blogs_collection.find(query).sort("created_at", -1).skip(skip).limit(limit))
    total = blogs_collection.count_documents(query)
    
    return {
        "blogs": [serialize_doc(blog) for blog in blogs],
        "total": total,
        "page": page,
        "pages": (total + limit - 1) // limit
    }

@router.get("/blogs/featured")
async def get_featured_blogs():
    blogs_collection = get_collection("blog_posts")
    blogs = list(blogs_collection.find({"featured": True}).sort("created_at", -1).limit(5))
    return [serialize_doc(blog) for blog in blogs]

@router.get("/blogs/trending")
async def get_trending_blogs(limit: int = Query(10, ge=1, le=50)):
    blogs_collection = get_collection("blog_posts")
    
    # Calculate trending score: (views * 0.7) + (likes * 0.3) with recent posts prioritized
    pipeline = [
        {
            "$addFields": {
                "trending_score": {
                    "$add": [
                        {"$multiply": [{"$ifNull": ["$views", 0]}, 0.7]},
                        {"$multiply": [{"$ifNull": ["$likes", 0]}, 0.3]}
                    ]
                }
            }
        },
        {"$sort": {"trending_score": -1, "created_at": -1}},
        {"$limit": limit}
    ]
    
    trending = list(blogs_collection.aggregate(pipeline))
    return [serialize_doc(blog) for blog in trending]

@router.get("/blogs/{blog_id}")
async def get_blog(blog_id: str):
    blogs_collection = get_collection("blog_posts")
    
    try:
        # Increment view count
        blogs_collection.update_one(
            {"_id": ObjectId(blog_id)},
            {"$inc": {"views": 1}}
        )
        
        blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found")
        return serialize_doc(blog)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/blogs")
async def create_blog(blog: BlogPostCreate, admin: bool = Depends(verify_admin)):
    blogs_collection = get_collection("blog_posts")
    
    blog_dict = blog.dict()
    blog_dict["created_at"] = datetime.utcnow()
    blog_dict["updated_at"] = datetime.utcnow()
    
    result = blogs_collection.insert_one(blog_dict)
    blog_dict["_id"] = str(result.inserted_id)
    
    return blog_dict

@router.put("/blogs/{blog_id}")
async def update_blog(blog_id: str, blog_update: BlogPostUpdate, admin: bool = Depends(verify_admin)):
    blogs_collection = get_collection("blog_posts")
    
    try:
        update_data = {k: v for k, v in blog_update.dict().items() if v is not None}
        update_data["updated_at"] = datetime.utcnow()
        
        result = blogs_collection.update_one(
            {"_id": ObjectId(blog_id)},
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Blog not found")
        
        blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
        return serialize_doc(blog)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/blogs/{blog_id}")
async def delete_blog(blog_id: str, admin: bool = Depends(verify_admin)):
    blogs_collection = get_collection("blog_posts")
    
    try:
        result = blogs_collection.delete_one({"_id": ObjectId(blog_id)})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Blog not found")
        
        return {"message": "Blog deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/blogs/{blog_id}/related")
async def get_related_blogs(blog_id: str, limit: int = Query(5, ge=1, le=20)):
    blogs_collection = get_collection("blog_posts")
    
    try:
        blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found")
        
        related_blogs = list(blogs_collection.find({
            "$and": [
                {"_id": {"$ne": ObjectId(blog_id)}},
                {
                    "$or": [
                        {"category": blog["category"]},
                        {"tags": {"$in": blog.get("tags", [])}}
                    ]
                }
            ]
        }).limit(limit))
        
        return [serialize_doc(blog) for blog in related_blogs]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/categories")
async def get_categories():
    categories_collection = get_collection("categories")
    categories = list(categories_collection.find())
    return [serialize_doc(cat) for cat in categories]

@router.get("/categories/{category_name}/posts")
async def get_posts_by_category(
    category_name: str,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    blogs_collection = get_collection("blog_posts")
    
    skip = (page - 1) * limit
    
    blogs = list(blogs_collection.find({"category": category_name}).sort("created_at", -1).skip(skip).limit(limit))
    total = blogs_collection.count_documents({"category": category_name})
    
    return {
        "blogs": [serialize_doc(blog) for blog in blogs],
        "total": total,
        "page": page,
        "pages": (total + limit - 1) // limit,
        "category": category_name
    }

@router.post("/categories")
async def create_category(category: CategoryModel, admin: bool = Depends(verify_admin)):
    categories_collection = get_collection("categories")
    
    category_dict = category.dict()
    result = categories_collection.insert_one(category_dict)
    category_dict["_id"] = str(result.inserted_id)
    
    return category_dict

@router.get("/tags")
async def get_tags():
    tags_collection = get_collection("tags")
    tags = list(tags_collection.find())
    return [serialize_doc(tag) for tag in tags]

@router.get("/tags/{tag_name}/posts")
async def get_posts_by_tag(
    tag_name: str,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    blogs_collection = get_collection("blog_posts")
    
    skip = (page - 1) * limit
    
    blogs = list(blogs_collection.find({"tags": tag_name}).sort("created_at", -1).skip(skip).limit(limit))
    total = blogs_collection.count_documents({"tags": tag_name})
    
    return {
        "blogs": [serialize_doc(blog) for blog in blogs],
        "total": total,
        "page": page,
        "pages": (total + limit - 1) // limit,
        "tag": tag_name
    }

@router.post("/tags")
async def create_tag(tag: TagModel, admin: bool = Depends(verify_admin)):
    tags_collection = get_collection("tags")
    
    tag_dict = tag.dict()
    result = tags_collection.insert_one(tag_dict)
    tag_dict["_id"] = str(result.inserted_id)
    
    return tag_dict

@router.get("/search")
async def search_blogs(q: str = Query(..., min_length=1)):
    blogs_collection = get_collection("blog_posts")
    
    blogs = list(blogs_collection.find({
        "$or": [
            {"title": {"$regex": q, "$options": "i"}},
            {"content": {"$regex": q, "$options": "i"}},
            {"tags": {"$regex": q, "$options": "i"}}
        ]
    }).sort("created_at", -1).limit(50))
    
    return [serialize_doc(blog) for blog in blogs]

@router.post("/ai/summarize")
async def ai_summarize(request: SummarizeRequest):
    result = summarize_blog(request.blog_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.post("/ai/chat")
async def ai_chat(request: ChatRequest):
    result = chat_with_blog(request.query, request.blog_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/latest-news")
async def get_latest_news(limit: int = Query(10, ge=1, le=50)):
    news_collection = get_collection("latest_news")
    news = list(news_collection.find().sort("created_at", -1).limit(limit))
    return [serialize_doc(item) for item in news]
