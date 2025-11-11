from database import get_collection
from datetime import datetime, timedelta
import random

def clear_collections():
    print("Clearing existing data...")
    get_collection("blog_posts").delete_many({})
    get_collection("categories").delete_many({})
    get_collection("tags").delete_many({})
    print("Data cleared successfully!")

def seed_categories():
    print("Seeding categories...")
    categories_collection = get_collection("categories")
    
    categories = [
        {"name": "Technology", "description": "Latest trends in technology and innovation"},
        {"name": "AI/ML", "description": "Artificial Intelligence and Machine Learning insights"},
        {"name": "Data Science", "description": "Data analysis, visualization, and insights"},
        {"name": "Web Development", "description": "Web technologies, frameworks, and best practices"},
        {"name": "Cloud Computing", "description": "Cloud platforms, DevOps, and infrastructure"},
        {"name": "Travel & Tourism", "description": "Travel guides, destinations, and tourism insights"},
        {"name": "Fashion & Style", "description": "Latest fashion trends and style tips"},
        {"name": "Automobiles", "description": "Cars, bikes, and automotive technology"},
        {"name": "Lifestyle", "description": "Lifestyle tips and personal development"},
        {"name": "Health & Wellness", "description": "Health tips, fitness, and wellness"},
        {"name": "Food & Recipes", "description": "Delicious recipes and food culture"},
        {"name": "Sports", "description": "Sports news, analysis, and updates"},
        {"name": "Finance & Investment", "description": "Financial advice and investment strategies"},
        {"name": "Entertainment", "description": "Movies, music, and entertainment news"}
    ]
    
    categories_collection.insert_many(categories)
    print(f"Inserted {len(categories)} categories")

def seed_tags():
    print("Seeding tags...")
    tags_collection = get_collection("tags")
    
    tags = [
        {"name": "Python"}, {"name": "JavaScript"}, {"name": "React"}, {"name": "Machine Learning"},
        {"name": "AI"}, {"name": "Tutorial"}, {"name": "Travel"}, {"name": "Fashion"},
        {"name": "Cars"}, {"name": "Health"}, {"name": "Food"}, {"name": "Sports"},
        {"name": "Finance"}, {"name": "Movies"}, {"name": "Beginner"}, {"name": "Advanced"}
    ]
    
    tags_collection.insert_many(tags)
    print(f"Inserted {len(tags)} tags")

def get_blog_data():
    authors = ["Dr. Sarah Chen", "Michael Roberts", "Emma Wilson", "James Anderson", "Lisa Thompson", 
               "David Kumar", "Rachel Green", "Alex Turner", "Maria Garcia", "Kevin Brown"]
    
    blogs = []
    day_offset = 0
    
    # AI/ML Blogs (8)
    ai_ml_blogs = [
        {
            "title": "The AI Revolution: How Machine Learning is Reshaping Our World",
            "content": """Artificial Intelligence and Machine Learning are no longer futuristic concepts—they're transforming industries today. From healthcare diagnostics to autonomous vehicles, AI is revolutionizing how we live and work.

Machine learning algorithms can now detect diseases earlier than human doctors, predict market trends with unprecedented accuracy, and even create art that rivals human creativity. The technology has matured from academic research to practical applications that touch billions of lives daily.

Key areas where AI is making the biggest impact include natural language processing, computer vision, and predictive analytics. Companies are leveraging these technologies to automate routine tasks, gain insights from massive datasets, and create personalized experiences for customers.

However, with great power comes great responsibility. As AI systems become more sophisticated, we must address ethical concerns around bias, privacy, and job displacement. The future of AI depends on our ability to develop these technologies responsibly while maximizing their benefits for society.

The next decade will see AI become even more integrated into our daily lives. From smart homes that anticipate our needs to AI assistants that truly understand context, the possibilities are endless. The question isn't whether AI will change the world—it's how we'll adapt to these changes.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Technology"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800",
            "views": random.randint(1000, 10000),
            "likes": random.randint(50, 800)
        },
        {
            "title": "Deep Learning Explained: Neural Networks for Beginners",
            "content": """Deep learning is a subset of machine learning that uses neural networks with multiple layers to progressively extract higher-level features from raw input. Think of it as teaching computers to learn by example, much like humans do.

At its core, a neural network consists of interconnected nodes (neurons) organized in layers. The input layer receives data, hidden layers process it through mathematical transformations, and the output layer produces predictions. Each connection has a weight that gets adjusted during training to improve accuracy.

The magic happens through backpropagation—an algorithm that calculates how much each weight contributed to the error and adjusts them accordingly. Over thousands of iterations, the network learns to recognize patterns and make accurate predictions.

Popular architectures include Convolutional Neural Networks (CNNs) for image processing, Recurrent Neural Networks (RNNs) for sequential data, and Transformers for natural language processing. Each architecture is optimized for specific types of problems.

Getting started with deep learning is easier than ever. Frameworks like TensorFlow and PyTorch provide high-level APIs that abstract away complex mathematics. Start with simple projects like image classification or sentiment analysis, then gradually tackle more complex problems as you build confidence.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Tutorial", "Beginner"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800",
            "views": random.randint(500, 5000),
            "likes": random.randint(30, 400)
        },
        {
            "title": "Natural Language Processing: Teaching Computers to Understand Human Language",
            "content": """Natural Language Processing (NLP) bridges the gap between human communication and computer understanding. It's the technology behind chatbots, translation services, and voice assistants that have become integral to our daily lives.

NLP combines computational linguistics with machine learning to process and analyze large amounts of natural language data. The field has evolved dramatically from rule-based systems to sophisticated neural networks that can understand context, sentiment, and even sarcasm.

Key NLP tasks include tokenization (breaking text into words), part-of-speech tagging, named entity recognition, sentiment analysis, and machine translation. Modern approaches use transformer models like BERT and GPT that have achieved human-level performance on many benchmarks.

The applications are vast and growing. Customer service chatbots handle millions of queries daily, content moderation systems keep online platforms safe, and translation tools break down language barriers. Healthcare providers use NLP to extract insights from medical records, while financial institutions analyze news sentiment to predict market movements.

The future of NLP is exciting. As models become more sophisticated, we're moving toward true language understanding where AI can engage in nuanced conversations, understand cultural context, and even demonstrate creativity in language use.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Python"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1655720828018-edd2daec9349?w=800",
            "views": random.randint(800, 7000),
            "likes": random.randint(40, 600)
        },
        {
            "title": "Computer Vision: How Machines Learn to See",
            "content": """Computer vision enables machines to derive meaningful information from digital images and videos. It's the technology that powers facial recognition, autonomous vehicles, and medical imaging analysis.

The field has progressed from simple edge detection to sophisticated deep learning models that can identify objects, understand scenes, and even generate realistic images. Convolutional Neural Networks (CNNs) revolutionized computer vision by automatically learning hierarchical features from images.

Modern computer vision systems can perform tasks that seemed impossible just a decade ago. They can detect cancer in medical scans with accuracy rivaling expert radiologists, enable cars to navigate complex traffic scenarios, and help visually impaired individuals understand their surroundings through audio descriptions.

Key techniques include image classification, object detection, semantic segmentation, and image generation. Transfer learning allows developers to leverage pre-trained models like ResNet and YOLO, making it easier to build custom vision applications without massive datasets.

The future holds even more promise. Advances in 3D vision, video understanding, and multimodal learning are opening new possibilities. From augmented reality experiences to robotic vision systems, computer vision will continue to transform how machines interact with the visual world.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Python", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1535378620166-273708d44e4c?w=800",
            "views": random.randint(600, 6000),
            "likes": random.randint(35, 500)
        },
        {
            "title": "Reinforcement Learning: Training AI Through Trial and Error",
            "content": """Reinforcement Learning (RL) is a paradigm where agents learn to make decisions by interacting with an environment and receiving rewards or penalties. It's how AlphaGo defeated world champions and how robots learn to walk.

Unlike supervised learning where models learn from labeled examples, RL agents learn through experience. They explore different actions, observe outcomes, and gradually develop strategies that maximize cumulative rewards. This trial-and-error approach mirrors how humans and animals learn.

The RL framework consists of an agent, environment, states, actions, and rewards. The agent observes the current state, takes an action, receives a reward, and transitions to a new state. The goal is to learn a policy—a mapping from states to actions—that maximizes long-term rewards.

Key algorithms include Q-Learning, which learns the value of state-action pairs, and Policy Gradient methods, which directly optimize the policy. Deep RL combines these approaches with neural networks to handle complex, high-dimensional problems.

Applications span gaming, robotics, resource management, and autonomous systems. RL is particularly powerful for problems where the optimal strategy isn't known in advance and must be discovered through interaction. As algorithms become more sample-efficient and stable, we'll see RL deployed in increasingly complex real-world scenarios.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800",
            "views": random.randint(400, 4000),
            "likes": random.randint(25, 350)
        },
        {
            "title": "Transfer Learning: Standing on the Shoulders of Giants",
            "content": """Transfer learning is a machine learning technique where knowledge gained from solving one problem is applied to a different but related problem. It's like how learning to play piano makes it easier to learn other keyboard instruments.

Training deep learning models from scratch requires massive datasets and computational resources. Transfer learning solves this by leveraging pre-trained models that have already learned useful features from large datasets. You can fine-tune these models for your specific task with much less data and time.

The approach is particularly powerful in computer vision and NLP. Models like ResNet, trained on millions of images, have learned to detect edges, textures, and complex patterns. By using these as starting points, you can build custom image classifiers with just hundreds of examples instead of millions.

In NLP, models like BERT and GPT have been pre-trained on vast text corpora, learning language structure and semantics. Fine-tuning them for specific tasks like sentiment analysis or question answering achieves state-of-the-art results with minimal additional training.

Transfer learning democratizes AI by making powerful models accessible to those without massive computational budgets. It accelerates development, improves performance, and enables applications that would otherwise be impractical. As pre-trained models continue to improve, transfer learning will remain a cornerstone of practical machine learning.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Tutorial"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800",
            "views": random.randint(500, 5000),
            "likes": random.randint(30, 400)
        },
        {
            "title": "Generative AI: Creating New Content with Machine Learning",
            "content": """Generative AI refers to models that can create new content—text, images, music, or code—that resembles human-created content. It's the technology behind AI art generators, chatbots, and code completion tools.

The breakthrough came with Generative Adversarial Networks (GANs), where two neural networks compete: a generator creates fake samples while a discriminator tries to distinguish real from fake. Through this adversarial process, the generator learns to create increasingly realistic outputs.

Transformer-based models like GPT have revolutionized text generation. They can write essays, answer questions, and even generate code. Diffusion models like DALL-E and Stable Diffusion create stunning images from text descriptions, democratizing creative expression.

Applications are exploding across industries. Content creators use AI to generate ideas and drafts, designers create concept art in seconds, and developers leverage code completion tools to boost productivity. In entertainment, AI generates game assets, music, and even entire virtual worlds.

However, generative AI raises important questions about creativity, copyright, and authenticity. As these tools become more powerful, society must grapple with their implications while harnessing their potential to augment human creativity rather than replace it.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Technology"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800",
            "views": random.randint(1200, 12000),
            "likes": random.randint(60, 900)
        },
        {
            "title": "MLOps: Bringing Machine Learning to Production",
            "content": """MLOps (Machine Learning Operations) is the practice of deploying, monitoring, and maintaining machine learning models in production. It bridges the gap between data science experimentation and reliable production systems.

Building a model is just the beginning. MLOps addresses challenges like model versioning, reproducibility, monitoring, and continuous improvement. It applies DevOps principles to machine learning, ensuring models remain accurate and reliable over time.

Key components include experiment tracking, model registry, automated testing, deployment pipelines, and monitoring systems. Tools like MLflow, Kubeflow, and cloud-native solutions help teams manage the entire ML lifecycle.

Model drift—when model performance degrades due to changing data patterns—is a critical concern. MLOps practices include monitoring for drift, automated retraining, and A/B testing to ensure models continue delivering value.

As organizations deploy more ML models, MLOps becomes essential. It enables teams to iterate faster, reduce errors, and scale ML initiatives. The field is rapidly evolving with new tools and best practices emerging to handle increasingly complex ML systems.""",
            "author": random.choice(authors),
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800",
            "views": random.randint(400, 4000),
            "likes": random.randint(25, 350)
        }
    ]
    
    for blog in ai_ml_blogs:
        blog["created_at"] = datetime.utcnow() - timedelta(days=day_offset)
        blog["updated_at"] = datetime.utcnow() - timedelta(days=day_offset)
        day_offset += 1
        blogs.append(blog)
    
    # Web Development Blogs (8)
    web_dev_blogs = [
        {
            "title": "React 19: Revolutionary Features Coming in 2025",
            "content": """React 19 is set to introduce groundbreaking features that will transform how we build web applications. From improved server components to enhanced performance optimizations, this release represents a major leap forward.

Server Components are becoming more powerful, allowing developers to fetch data and render components on the server without sending JavaScript to the client. This dramatically improves initial page load times and reduces bundle sizes.

The new React Compiler automatically optimizes your components, eliminating the need for manual memoization in most cases. It analyzes your code and applies optimizations that previously required careful use of useMemo and useCallback.

Actions provide a new way to handle form submissions and data mutations. They integrate seamlessly with Suspense and error boundaries, making it easier to build robust, user-friendly forms with loading and error states.

The improved Suspense implementation supports more use cases, including better integration with streaming SSR and more granular control over loading states. Combined with the new use hook, data fetching becomes more intuitive and powerful.

These changes represent React's evolution toward better performance, simpler code, and improved developer experience. Early adopters are already seeing significant benefits in their applications.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["React", "JavaScript", "Tutorial"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800",
            "views": random.randint(1000, 10000),
            "likes": random.randint(50, 800)
        },
        {
            "title": "Modern JavaScript: ES2024 Features Every Developer Should Know",
            "content": """JavaScript continues its rapid evolution with ES2024 bringing powerful new features that make code more expressive and maintainable. Let's explore the most impactful additions.

The new Array grouping methods (groupBy and groupByToMap) simplify organizing data. Instead of writing complex reduce operations, you can now group array elements with a simple callback function.

Promise.withResolvers() provides a cleaner way to create promises with external resolve and reject functions. This is particularly useful for integrating promises with callback-based APIs or event handlers.

RegExp v flag enables set notation and properties of strings, making complex text matching more intuitive. Combined with Unicode property escapes, it's now easier to work with international text.

ArrayBuffer transfer methods allow efficient memory management when working with binary data. This is crucial for performance-sensitive applications like image processing or WebAssembly integration.

These features build on JavaScript's strengths while addressing common pain points. As browser support improves, they'll become essential tools in every developer's toolkit.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["JavaScript", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?w=800",
            "views": random.randint(800, 8000),
            "likes": random.randint(40, 600)
        },
        {
            "title": "Building Scalable APIs with Node.js and Express",
            "content": """Node.js and Express remain the go-to choice for building fast, scalable APIs. This guide covers best practices for creating production-ready backend services.

Architecture matters. Organize your code into clear layers: routes handle HTTP concerns, controllers contain business logic, and services manage data access. This separation makes code testable and maintainable.

Middleware is Express's superpower. Use it for authentication, logging, error handling, and request validation. Custom middleware can transform how your application processes requests, making cross-cutting concerns easy to manage.

Error handling requires careful attention. Implement centralized error handling middleware, use async/await with try-catch blocks, and return consistent error responses. Proper error handling prevents crashes and provides better debugging information.

Security is paramount. Use helmet for security headers, implement rate limiting, validate all inputs, and never trust client data. Regular security audits and dependency updates keep your API safe.

Performance optimization includes database query optimization, caching strategies, and proper use of async operations. Monitor your API with tools like PM2 or New Relic to identify bottlenecks.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["JavaScript", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800",
            "views": random.randint(600, 6000),
            "likes": random.randint(35, 500)
        },
        {
            "title": "TypeScript Best Practices for Large-Scale Applications",
            "content": """TypeScript has become essential for large-scale JavaScript applications. These best practices will help you leverage TypeScript's full power while avoiding common pitfalls.

Type safety is TypeScript's core benefit. Use strict mode, avoid 'any' types, and leverage type inference. Well-typed code catches bugs at compile time and serves as living documentation.

Interfaces and types serve different purposes. Use interfaces for object shapes that might be extended, and type aliases for unions, intersections, and complex types. Understanding when to use each improves code clarity.

Generics enable reusable, type-safe code. They're essential for utility functions, data structures, and API clients. Master generic constraints and conditional types to write more flexible code.

Organize types in dedicated files or alongside implementation. For shared types, create a types directory. This makes types easy to find and reuse across your application.

Leverage utility types like Partial, Pick, Omit, and Record. They reduce boilerplate and make type transformations explicit. Custom utility types can encode business rules at the type level.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["JavaScript", "Tutorial", "Advanced"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800",
            "views": random.randint(900, 9000),
            "likes": random.randint(45, 700)
        },
        {
            "title": "Web Performance: Making Your Site Lightning Fast",
            "content": """Website performance directly impacts user experience, SEO, and conversion rates. Learn how to optimize every aspect of your web application for maximum speed.

Core Web Vitals are Google's performance metrics: Largest Contentful Paint (LCP), First Input Delay (FID), and Cumulative Layout Shift (CLS). Optimizing these metrics improves both user experience and search rankings.

Image optimization is low-hanging fruit. Use modern formats like WebP and AVIF, implement lazy loading, serve responsive images, and compress aggressively. Images often account for most page weight.

JavaScript optimization includes code splitting, tree shaking, and deferring non-critical scripts. Modern bundlers like Vite and esbuild make this easier than ever. Measure your bundle size and eliminate unused code.

CSS optimization involves removing unused styles, minifying CSS, and using critical CSS inline. Tools like PurgeCSS automatically remove unused styles from your production builds.

Caching strategies dramatically improve repeat visit performance. Use service workers for offline support, implement proper cache headers, and leverage CDNs for static assets.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["JavaScript", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800",
            "views": random.randint(700, 7000),
            "likes": random.randint(40, 550)
        },
        {
            "title": "GraphQL: Modern API Development",
            "content": """GraphQL is revolutionizing how we build and consume APIs. Unlike REST, GraphQL lets clients request exactly the data they need, eliminating over-fetching and under-fetching.

The schema defines your API's capabilities. It's strongly typed, self-documenting, and serves as a contract between frontend and backend. Tools generate documentation and enable powerful IDE features.

Queries fetch data, mutations modify it, and subscriptions enable real-time updates. This clear separation makes APIs intuitive and predictable. Clients compose queries to fetch related data in a single request.

Resolvers are functions that fetch data for each field. They can fetch from databases, call other APIs, or perform computations. Efficient resolver implementation is key to GraphQL performance.

DataLoader solves the N+1 query problem by batching and caching database requests. It's essential for production GraphQL servers, dramatically improving performance.

GraphQL shines for complex data requirements, mobile applications, and microservices. While it adds complexity, the benefits often outweigh the costs for the right use cases.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["JavaScript", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800",
            "views": random.randint(500, 5000),
            "likes": random.randint(30, 400)
        },
        {
            "title": "Next.js 14: Full-Stack React Framework",
            "content": """Next.js 14 brings powerful features for building full-stack React applications. From server components to improved routing, it's the most capable version yet.

Server Components are now stable, enabling zero-JavaScript components that render on the server. This dramatically reduces bundle sizes and improves initial page load. Client components handle interactivity where needed.

The App Router provides file-based routing with layouts, loading states, and error boundaries built in. Nested layouts enable sophisticated page structures without prop drilling.

Server Actions simplify data mutations. Write server-side functions that can be called directly from client components, with automatic serialization and type safety. No API routes needed for simple mutations.

Image optimization is automatic with the Image component. It serves responsive images, lazy loads by default, and uses modern formats. This alone can significantly improve performance.

Deployment is seamless with Vercel, but Next.js works anywhere Node.js runs. The framework's flexibility makes it suitable for everything from static sites to complex web applications.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["React", "JavaScript", "Tutorial"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800",
            "views": random.randint(1100, 11000),
            "likes": random.randint(55, 850)
        },
        {
            "title": "Web Security: Protecting Your Applications",
            "content": """Web security is not optional. Every application must protect against common vulnerabilities that attackers actively exploit. This guide covers essential security practices.

XSS (Cross-Site Scripting) allows attackers to inject malicious scripts. Prevent it by sanitizing user input, using Content Security Policy headers, and leveraging framework protections. Never trust user data.

CSRF (Cross-Site Request Forgery) tricks users into performing unwanted actions. Use CSRF tokens, SameSite cookies, and verify request origins. Modern frameworks provide CSRF protection out of the box.

SQL Injection occurs when user input is concatenated into SQL queries. Always use parameterized queries or ORMs. Never build SQL strings with user input.

Authentication and authorization must be robust. Use established libraries, implement proper session management, and never roll your own crypto. Multi-factor authentication adds crucial security.

Regular security audits, dependency updates, and penetration testing identify vulnerabilities before attackers do. Security is an ongoing process, not a one-time task.""",
            "author": random.choice(authors),
            "category": "Web Development",
            "tags": ["JavaScript", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800",
            "views": random.randint(600, 6000),
            "likes": random.randint(35, 500)
        }
    ]
    
    for blog in web_dev_blogs:
        blog["created_at"] = datetime.utcnow() - timedelta(days=day_offset)
        blog["updated_at"] = datetime.utcnow() - timedelta(days=day_offset)
        day_offset += 1
        blogs.append(blog)
    
    return blogs, day_offset

def main():
    print("=== Starting Database Seed ===")
    clear_collections()
    seed_categories()
    seed_tags()
    
    blogs, _ = get_blog_data()
    
    blogs_collection = get_collection("blog_posts")
    blogs_collection.insert_many(blogs)
    print(f"Inserted {len(blogs)} blog posts")
    
    print("=== Seed completed successfully! ===")

if __name__ == "__main__":
    main()
