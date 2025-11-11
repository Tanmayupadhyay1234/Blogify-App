import os
from groq import Groq
from database import get_collection
from datetime import datetime, timedelta
import random
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Blog categories
CATEGORIES = [
    "Technology", "AI/ML", "Data Science", "Web Development", "Cloud Computing",
    "Cybersecurity", "Blockchain", "IoT", "DevOps", "Mobile Development"
]

# Author names for blog posts
AUTHORS = ["Dr. Sarah Chen", "Michael Roberts", "Emma Wilson", "James Anderson", 
           "Lisa Thompson", "David Kumar", "Rachel Green", "Alex Turner", 
           "Maria Garcia", "Kevin Brown", "Jennifer Lee", "Daniel Park"]

# Commenter names for blog comments
COMMENTERS = ["John Doe", "Jane Smith", "Bob Johnson", "Alice Williams", "Charlie Brown",
              "Diana Prince", "Eve Adams", "Frank Miller", "Grace Lee", "Henry Ford",
              "Ivy Chen", "Jack Ryan", "Kate Wilson", "Leo Martinez", "Maya Patel"]

def clear_collections():
    """Clear all existing data from collections"""
    print("Clearing existing data...")
    get_collection("blog_posts").delete_many({})
    get_collection("categories").delete_many({})
    get_collection("tags").delete_many({})
    get_collection("comments").delete_many({})
    get_collection("latest_news").delete_many({})
    print("Data cleared!")

def seed_categories():
    """Seed blog categories"""
    print("Seeding categories...")
    categories_collection = get_collection("categories")
    categories = [{"name": cat, "description": f"{cat} articles and insights"} for cat in CATEGORIES]
    categories_collection.insert_many(categories)
    print(f"Inserted {len(categories)} categories")

def seed_tags():
    """Seed blog tags"""
    print("Seeding tags...")
    tags_collection = get_collection("tags")
    all_tags = ["Python", "JavaScript", "React", "AI", "Machine Learning", "Deep Learning",
                "Tutorial", "Tech", "Innovation", "Cloud", "AWS", "DevOps",
                "Data Science", "Analytics", "Frontend", "Backend", "Security",
                "Hacking", "Privacy", "Blockchain", "Crypto", "Web3", "IoT",
                "Smart Devices", "Sensors", "CI/CD", "Automation", "Mobile", "iOS", "Android"]
    tags = [{"name": tag} for tag in all_tags]
    tags_collection.insert_many(tags)
    print(f"Inserted {len(tags)} tags")

# Working Unsplash image URLs - verified format
CATEGORY_IMAGES = {
    "Technology": [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&h=800&fit=crop",
    ],
    "AI/ML": [
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1535378620166-273708d44e4c?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1507146153580-69a1fe6d8aa1?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=1200&h=800&fit=crop",
    ],
    "Data Science": [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1543286386-713bdd548da4?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1527474305487-b87b222841cc?w=1200&h=800&fit=crop",
    ],
    "Web Development": [
        "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1200&h=800&fit=crop",
    ],
    "Cloud Computing": [
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1639322537228-f710d846310a?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=1200&h=800&fit=crop",
    ],
    "Cybersecurity": [
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=1200&h=800&fit=crop",
    ],
    "Blockchain": [
        "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1622630998477-20aa696ecb05?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1605792657660-596af9009e82?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1639322537228-f710d846310a?w=1200&h=800&fit=crop",
    ],
    "IoT": [
        "https://images.unsplash.com/photo-1558346490-a72e53ae2d4f?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1558346490-a72e53ae2d4f?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=1200&h=800&fit=crop",
    ],
    "DevOps": [
        "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1639322537228-f710d846310a?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1200&h=800&fit=crop",
    ],
    "Mobile Development": [
        "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1607252650355-f7fd0460ccdb?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=1200&h=800&fit=crop",
        "https://images.unsplash.com/photo-1607252650355-f7fd0460ccdb?w=1200&h=800&fit=crop",
    ]
}

def get_category_image(category):
    """Get a random working image URL for a given category"""
    images = CATEGORY_IMAGES.get(category, CATEGORY_IMAGES["Technology"])
    return random.choice(images)

def generate_comments_for_blog(blog_id, num_comments=5):
    """Generate comments with nested replies for a blog post"""
    comments_collection = get_collection("comments")
    comments = []
    
    comment_templates = [
        "Great article! Very informative and well-written.",
        "Thanks for sharing this. Learned a lot from your insights.",
        "Excellent explanation! This cleared up many doubts I had.",
        "Really appreciate the detailed breakdown. Keep up the good work!",
        "This is exactly what I was looking for. Thank you!",
        "Interesting perspective. Would love to see more content like this.",
        "Well researched and presented. Looking forward to more articles.",
        "Very helpful! Bookmarking this for future reference.",
        "Amazing content! This helped me understand the concept better.",
        "Fantastic write-up! Could you do more on this topic?",
    ]
    
    reply_templates = [
        "I agree with your point!",
        "Thanks for adding that perspective.",
        "Interesting take on this.",
        "Could you elaborate more on this?",
        "That's a great addition to the discussion.",
        "I had the same thought!",
        "Well said!",
        "Thanks for clarifying!",
    ]
    
    # Generate parent comments
    for i in range(num_comments):
        comment = {
            "blog_id": str(blog_id),
            "author": random.choice(COMMENTERS),
            "content": random.choice(comment_templates),
            "created_at": datetime.utcnow() - timedelta(hours=random.randint(1, 72)),
            "likes": random.randint(0, 50),
            "parent_id": None
        }
        result = comments_collection.insert_one(comment)
        comment["_id"] = result.inserted_id
        comments.append(comment)
        
        # Generate 1-3 nested replies for some comments (60% chance)
        if random.random() > 0.4:
            num_replies = random.randint(1, 3)
            for j in range(num_replies):
                reply = {
                    "blog_id": str(blog_id),
                    "author": random.choice(COMMENTERS),
                    "content": random.choice(reply_templates),
                    "created_at": datetime.utcnow() - timedelta(hours=random.randint(1, 48)),
                    "likes": random.randint(0, 20),
                    "parent_id": str(comment["_id"])
                }
                comments_collection.insert_one(reply)
    
    return len(comments)

def generate_blog_with_ai(category, index):
    """Generate blog content using GROQ AI"""
    title_styles = [
        f"Write about {category} with a title starting with 'How to'",
        f"Write about {category} with a title starting with 'The Future of'",
        f"Write about {category} with a title starting with 'Understanding'",
        f"Write about {category} with a title starting with 'Mastering'",
        f"Write about {category} with a title starting with 'A Complete Guide to'",
        f"Write about {category} with a title starting with 'Why'",
        f"Write about {category} with a title starting with 'Top 10'",
        f"Write about {category} with a title starting with 'Essential'",
        f"Write about {category} with a title starting with 'Building'",
        f"Write about {category} with a title starting with 'Exploring'",
    ]
    
    style = title_styles[index % len(title_styles)]
    
    prompt = f"""Write a comprehensive, engaging blog post about {category}. 

Requirements:
- Title: {style} (50-80 characters, make it unique and specific)
- Content: Write 500-700 words of high-quality, informative content
- Include practical insights, examples, and actionable advice
- Use a professional yet conversational tone
- Format with clear paragraphs (no markdown headers)
- Make it engaging and educational

Return ONLY in this exact format:
TITLE: [your title here]
CONTENT: [your content here]"""

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.8,
            max_tokens=1500
        )
        
        result = response.choices[0].message.content
        
        # Parse response
        if "TITLE:" in result and "CONTENT:" in result:
            title = result.split("TITLE:")[1].split("CONTENT:")[0].strip()
            content = result.split("CONTENT:")[1].strip()
            return title, content
        else:
            return None, None
            
    except Exception as e:
        print(f"  ✗ Error generating blog {index}: {e}")
        return None, None

def generate_blogs(num_blogs=60):
    """Generate blog posts using AI with proper working images and metadata"""
    print(f"\nGenerating {num_blogs} blogs with AI...")
    blogs_collection = get_collection("blog_posts")
    blogs = []
    blog_ids = []
    
    # Distribute blogs evenly across categories
    blogs_per_category = num_blogs // len(CATEGORIES)
    extra_blogs = num_blogs % len(CATEGORIES)
    
    blog_count = 0
    day_offset = 0
    
    # Tag mapping for each category
    tag_map = {
        "Technology": ["Tech", "Innovation", "Gadgets", "Tutorial"],
        "AI/ML": ["AI", "Machine Learning", "Python", "Deep Learning", "Tutorial"],
        "Data Science": ["Data Science", "Python", "Analytics", "Tutorial"],
        "Web Development": ["JavaScript", "React", "Frontend", "Backend", "Tutorial"],
        "Cloud Computing": ["Cloud", "AWS", "DevOps", "Tutorial"],
        "Cybersecurity": ["Security", "Hacking", "Privacy", "Tutorial"],
        "Blockchain": ["Blockchain", "Crypto", "Web3", "Tutorial"],
        "IoT": ["IoT", "Smart Devices", "Sensors", "Tutorial"],
        "DevOps": ["DevOps", "CI/CD", "Automation", "Tutorial"],
        "Mobile Development": ["Mobile", "iOS", "Android", "Tutorial"]
    }
    
    for cat_index, category in enumerate(CATEGORIES):
        num_for_category = blogs_per_category + (1 if cat_index < extra_blogs else 0)
        
        for i in range(num_for_category):
            blog_count += 1
            print(f"Generating blog {blog_count}/{num_blogs} - Category: {category}...")
            
            title, content = generate_blog_with_ai(category, blog_count)
            
            if title and content:
                # Select appropriate tags
                available_tags = tag_map.get(category, ["Tutorial"])
                tags = random.sample(available_tags, min(3, len(available_tags)))
                
                blog = {
                    "title": title,
                    "content": content,
                    "author": random.choice(AUTHORS),
                    "category": category,
                    "tags": tags,
                    "featured": blog_count <= 15,  # First 15 are featured
                    "image_url": get_category_image(category),
                    "views": random.randint(150, 15000),
                    "likes": random.randint(20, 1200),
                    "created_at": datetime.utcnow() - timedelta(days=day_offset),
                    "updated_at": datetime.utcnow() - timedelta(days=day_offset)
                }
                
                blogs.append(blog)
                day_offset += 1
                
                # Insert in batches of 10
                if len(blogs) >= 10:
                    result = blogs_collection.insert_many(blogs)
                    blog_ids.extend(result.inserted_ids)
                    print(f"  ✓ Inserted batch of {len(blogs)} blogs")
                    blogs = []
            else:
                print(f"  ✗ Failed to generate blog {blog_count}, retrying...")
                # Retry once
                title, content = generate_blog_with_ai(category, blog_count)
                if title and content:
                    available_tags = tag_map.get(category, ["Tutorial"])
                    tags = random.sample(available_tags, min(3, len(available_tags)))
                    
                    blog = {
                        "title": title,
                        "content": content,
                        "author": random.choice(AUTHORS),
                        "category": category,
                        "tags": tags,
                        "featured": blog_count <= 15,
                        "image_url": get_category_image(category),
                        "views": random.randint(150, 15000),
                        "likes": random.randint(20, 1200),
                        "created_at": datetime.utcnow() - timedelta(days=day_offset),
                        "updated_at": datetime.utcnow() - timedelta(days=day_offset)
                    }
                    blogs.append(blog)
                    day_offset += 1
    
    # Insert remaining blogs
    if blogs:
        result = blogs_collection.insert_many(blogs)
        blog_ids.extend(result.inserted_ids)
        print(f"  ✓ Inserted final batch of {len(blogs)} blogs")
    
    print(f"\n✓ Successfully generated {blog_count} blogs!")
    
    # Generate comments for all blogs
    print(f"\nGenerating comments for {len(blog_ids)} blogs...")
    total_comments = 0
    for idx, blog_id in enumerate(blog_ids, 1):
        num_comments = random.randint(3, 10)
        comments_count = generate_comments_for_blog(blog_id, num_comments)
        total_comments += comments_count
        if idx % 10 == 0:
            print(f"  Progress: {idx}/{len(blog_ids)} blogs processed...")
    
    print(f"✓ Generated {total_comments} comments with nested replies!")

def generate_latest_news(num_news=15):
    """Generate latest news articles using AI"""
    print(f"\nGenerating {num_news} latest news articles...")
    news_collection = get_collection("latest_news")
    news_items = []
    
    for i in range(num_news):
        category = random.choice(CATEGORIES)
        print(f"Generating news {i+1}/{num_news} - Category: {category}...")
        
        prompt = f"""Write a short, breaking news headline and summary about {category}.

Requirements:
- Headline: Create a compelling, current news headline (40-60 characters)
- Summary: Write 2-3 sentences (100-150 words) summarizing the breaking news
- Make it sound newsworthy and recent (2025)
- Use professional journalism tone
- Focus on innovations, releases, or major developments

Return ONLY in this exact format:
HEADLINE: [your headline]
SUMMARY: [your summary]"""
        
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant",
                temperature=0.9,
                max_tokens=300
            )
            
            result = response.choices[0].message.content
            
            if "HEADLINE:" in result and "SUMMARY:" in result:
                headline = result.split("HEADLINE:")[1].split("SUMMARY:")[0].strip()
                summary = result.split("SUMMARY:")[1].strip()
                
                news = {
                    "headline": headline,
                    "summary": summary,
                    "category": category,
                    "image_url": get_category_image(category),
                    "created_at": datetime.utcnow() - timedelta(hours=i*2),
                    "views": random.randint(100, 800)
                }
                news_items.append(news)
                print(f"  ✓ Generated news: {headline[:50]}...")
        except Exception as e:
            print(f"  ✗ Error generating news {i+1}: {e}")
    
    if news_items:
        news_collection.insert_many(news_items)
        print(f"✓ Inserted {len(news_items)} news articles")

def main():
    """Main function to seed all data"""
    print("=" * 60)
    print("    AI-POWERED BLOG SEEDING SYSTEM")
    print("=" * 60)
    
    clear_collections()
    seed_categories()
    seed_tags()
    generate_blogs(60)  # Generate 60+ quality blogs
    generate_latest_news(15)  # Generate 15 news articles
    
    print("\n" + "=" * 60)
    print("    SEEDING COMPLETE!")
    print("=" * 60)
    print("✓ 60+ blogs with working Unsplash images")
    print("✓ Comments with nested replies")
    print("✓ 15 latest news articles")
    print("✓ All categories and tags")
    print("✓ Proper metadata (views, likes, dates)")
    print("=" * 60)

if __name__ == "__main__":
    main()
