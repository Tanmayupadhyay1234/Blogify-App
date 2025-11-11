import os
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType, utility
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)

def connect_milvus():
    try:
        connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)
        return True
    except Exception as e:
        print(f"Milvus connection failed: {e}")
        return False

def create_blog_collection():
    if utility.has_collection("blog_embeddings"):
        return Collection("blog_embeddings")
    
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="blog_id", dtype=DataType.VARCHAR, max_length=100),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)
    ]
    schema = CollectionSchema(fields, description="Blog post embeddings")
    collection = Collection("blog_embeddings", schema)
    
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }
    collection.create_index("embedding", index_params)
    return collection

def generate_embedding(text: str):
    """Generate embedding using sentence-transformers via local model or API"""
    try:
        # Fallback: Use simple text representation (replace with actual embedding model)
        # For production, use sentence-transformers or OpenAI embeddings
        words = text.lower().split()[:384]
        embedding = [hash(word) % 1000 / 1000.0 for word in words]
        embedding.extend([0.0] * (384 - len(embedding)))
        return embedding[:384]
    except Exception as e:
        print(f"Embedding generation failed: {e}")
        return [0.0] * 384

def store_blog_embedding(blog_id: str, title: str, content: str):
    if not connect_milvus():
        return None
    
    collection = create_blog_collection()
    text = f"{title} {content[:500]}"
    embedding = generate_embedding(text)
    
    data = [[blog_id], [embedding]]
    collection.insert(data)
    collection.load()
    return True

def search_similar_blogs(blog_id: str, limit: int = 5):
    if not connect_milvus():
        return []
    
    collection = create_blog_collection()
    collection.load()
    
    # Get embedding for current blog
    results = collection.query(expr=f'blog_id == "{blog_id}"', output_fields=["embedding"])
    if not results:
        return []
    
    query_embedding = results[0]["embedding"]
    
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param=search_params,
        limit=limit + 1,
        output_fields=["blog_id"]
    )
    
    similar_ids = [hit.entity.get("blog_id") for hit in results[0] if hit.entity.get("blog_id") != blog_id]
    return similar_ids[:limit]
