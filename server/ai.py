import os
from groq import Groq
from dotenv import load_dotenv
from database import get_collection
from bson import ObjectId

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def summarize_blog(blog_id: str):
    blogs_collection = get_collection("blog_posts")
    
    try:
        blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
        
        if not blog:
            return {"error": "Blog not found"}
        
        prompt = f"""Please provide a concise summary of the following blog post.
        
Title: {blog['title']}
Category: {blog['category']}
Content: {blog['content']}

Provide a 2-3 sentence summary that captures the key points."""

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=200,
        )
        
        summary = chat_completion.choices[0].message.content
        
        return {
            "blog_id": blog_id,
            "title": blog["title"],
            "summary": summary
        }
        
    except Exception as e:
        return {"error": f"Error generating summary: {str(e)}"}

def chat_with_blog(query: str, blog_id: str = None):
    blogs_collection = get_collection("blog_posts")
    
    try:
        context = ""
        
        if blog_id:
            blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
            if blog:
                context = f"""
Blog Context:
Title: {blog['title']}
Category: {blog['category']}
Tags: {', '.join(blog.get('tags', []))}
Content: {blog['content'][:1000]}...
"""
        
        prompt = f"""{context}

User Question: {query}

Please provide a helpful and informative answer based on the blog content and your knowledge."""

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=500,
        )
        
        answer = chat_completion.choices[0].message.content
        
        return {
            "query": query,
            "answer": answer,
            "blog_id": blog_id
        }
        
    except Exception as e:
        return {"error": f"Error processing chat: {str(e)}"}
