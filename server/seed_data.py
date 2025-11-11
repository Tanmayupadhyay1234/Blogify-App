from database import get_collection
from datetime import datetime, timedelta
import random

def clear_collections():
    print("Clearing existing data...")
    get_collection("blog_posts").delete_many({})
    get_collection("categories").delete_many({})
    get_collection("tags").delete_many({})
    get_collection("users").delete_many({})
    print("Data cleared successfully!")

def seed_categories():
    print("Seeding categories...")
    categories_collection = get_collection("categories")
    
    categories = [
        {
            "name": "Technology",
            "description": "Latest trends in technology and innovation",
            "tags": ["Tech", "Innovation", "Gadgets"]
        },
        {
            "name": "AI/ML",
            "description": "Artificial Intelligence and Machine Learning insights",
            "tags": ["AI", "Machine Learning", "Deep Learning", "Neural Networks"]
        },
        {
            "name": "Data Science",
            "description": "Data analysis, visualization, and insights",
            "tags": ["Data", "Analytics", "Python", "Visualization"]
        },
        {
            "name": "Web Development",
            "description": "Web technologies, frameworks, and best practices",
            "tags": ["JavaScript", "React", "Frontend", "Backend"]
        },
        {
            "name": "Cloud Computing",
            "description": "Cloud platforms, DevOps, and infrastructure",
            "tags": ["AWS", "Cloud", "DevOps", "Infrastructure"]
        },
        {
            "name": "Travel & Tourism",
            "description": "Travel guides, destinations, and tourism insights",
            "tags": ["Travel", "Tourism", "Destinations", "Adventure"]
        },
        {
            "name": "Fashion & Style",
            "description": "Latest fashion trends and style tips",
            "tags": ["Fashion", "Style", "Trends", "Beauty"]
        },
        {
            "name": "Automobiles",
            "description": "Cars, bikes, and automotive technology",
            "tags": ["Cars", "Bikes", "Automotive", "Reviews"]
        },
        {
            "name": "Lifestyle",
            "description": "Lifestyle tips and personal development",
            "tags": ["Lifestyle", "Wellness", "Personal Growth"]
        },
        {
            "name": "Health & Wellness",
            "description": "Health tips, fitness, and wellness",
            "tags": ["Health", "Fitness", "Wellness", "Nutrition"]
        },
        {
            "name": "Food & Recipes",
            "description": "Delicious recipes and food culture",
            "tags": ["Food", "Recipes", "Cooking", "Cuisine"]
        },
        {
            "name": "Sports",
            "description": "Sports news, analysis, and updates",
            "tags": ["Sports", "Football", "Cricket", "Fitness"]
        },
        {
            "name": "Finance & Investment",
            "description": "Financial advice and investment strategies",
            "tags": ["Finance", "Investment", "Money", "Stocks"]
        },
        {
            "name": "Entertainment",
            "description": "Movies, music, and entertainment news",
            "tags": ["Movies", "Music", "Entertainment", "TV"]
        }
    ]
    
    categories_collection.insert_many(categories)
    print(f"Inserted {len(categories)} categories")

def seed_tags():
    print("Seeding tags...")
    tags_collection = get_collection("tags")
    
    tags = [
        {"name": "Python"},
        {"name": "JavaScript"},
        {"name": "React"},
        {"name": "Machine Learning"},
        {"name": "Deep Learning"},
        {"name": "AI"},
        {"name": "Data Science"},
        {"name": "Cloud"},
        {"name": "DevOps"},
        {"name": "FastAPI"},
        {"name": "MongoDB"},
        {"name": "Tutorial"},
        {"name": "Best Practices"},
        {"name": "Beginner"},
        {"name": "Advanced"}
    ]
    
    tags_collection.insert_many(tags)
    print(f"Inserted {len(tags)} tags")

def seed_blogs():
    print("Seeding blog posts...")
    blogs_collection = get_collection("blog_posts")
    
    blogs = [
        {
            "title": "Getting Started with Machine Learning in 2025",
            "content": """Machine learning has become an essential skill for developers and data scientists. In this comprehensive guide, we'll explore the fundamentals of ML and how to get started with your first project.

**What is Machine Learning?**
Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.

**Key Concepts:**
1. Supervised Learning - Training models with labeled data
2. Unsupervised Learning - Finding patterns in unlabeled data
3. Reinforcement Learning - Learning through trial and error

**Getting Started:**
Start with Python and libraries like scikit-learn, TensorFlow, and PyTorch. Practice with datasets from Kaggle and build small projects to solidify your understanding.

**Conclusion:**
Machine learning is an exciting field with endless possibilities. Start small, stay consistent, and keep learning!""",
            "author": "Sarah Johnson",
            "category": "AI/ML",
            "tags": ["Machine Learning", "AI", "Python", "Tutorial", "Beginner"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=1),
            "updated_at": datetime.utcnow() - timedelta(days=1)
        },
        {
            "title": "React 18: New Features and Performance Improvements",
            "content": """React 18 introduces several groundbreaking features that enhance application performance and developer experience. Let's dive into what's new.

**Concurrent Rendering:**
React 18 introduces concurrent rendering, allowing React to work on multiple tasks simultaneously. This improves responsiveness and user experience.

**Automatic Batching:**
React now automatically batches state updates, reducing re-renders and improving performance across your application.

**New Hooks:**
- useTransition: Mark updates as non-urgent
- useDeferredValue: Defer updating less important parts of the UI
- useId: Generate unique IDs for accessibility

**Suspense Improvements:**
Server-side rendering with Suspense is now fully supported, enabling better code splitting and loading states.

**Migration Tips:**
Update to React 18 gradually. Most applications will work without changes, but review the official migration guide for best practices.""",
            "author": "Michael Chen",
            "category": "Web Development",
            "tags": ["React", "JavaScript", "Frontend", "Tutorial"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=2),
            "updated_at": datetime.utcnow() - timedelta(days=2)
        },
        {
            "title": "Python FastAPI: Building High-Performance APIs",
            "content": """FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints. It's becoming the go-to choice for API development.

**Why FastAPI?**
1. Fast: Very high performance, on par with NodeJS and Go
2. Type hints: Automatic validation and documentation
3. Async support: Built-in support for async/await
4. Auto documentation: Interactive API docs with Swagger UI

**Creating Your First API:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

**Key Features:**
- Automatic data validation using Pydantic
- OAuth2 authentication support
- Dependency injection system
- WebSocket support

**Best Practices:**
Use proper project structure, implement error handling, add comprehensive tests, and leverage FastAPI's dependency injection for clean code.""",
            "author": "David Rodriguez",
            "category": "Web Development",
            "tags": ["Python", "FastAPI", "Backend", "Tutorial", "Advanced"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=3),
            "updated_at": datetime.utcnow() - timedelta(days=3)
        },
        {
            "title": "Deep Learning Fundamentals: Neural Networks Explained",
            "content": """Deep learning has revolutionized AI, powering everything from image recognition to natural language processing. Let's understand how neural networks work.

**What are Neural Networks?**
Neural networks are computing systems inspired by biological neural networks in animal brains. They consist of layers of interconnected nodes (neurons).

**Architecture:**
1. Input Layer: Receives the input data
2. Hidden Layers: Process information
3. Output Layer: Produces the final result

**Activation Functions:**
- ReLU: Most common for hidden layers
- Sigmoid: Binary classification
- Softmax: Multi-class classification

**Training Process:**
Neural networks learn through backpropagation, adjusting weights to minimize loss. This requires:
- Quality training data
- Proper network architecture
- Appropriate learning rate
- Regularization techniques

**Applications:**
Image classification, object detection, speech recognition, natural language processing, and more.""",
            "author": "Emily Watson",
            "category": "AI/ML",
            "tags": ["Deep Learning", "Neural Networks", "AI", "Tutorial"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=4),
            "updated_at": datetime.utcnow() - timedelta(days=4)
        },
        {
            "title": "Cloud Computing with AWS: A Comprehensive Guide",
            "content": """Amazon Web Services (AWS) is the world's most comprehensive cloud platform. Learn how to leverage AWS for your applications.

**Core Services:**
1. EC2: Virtual servers in the cloud
2. S3: Object storage service
3. RDS: Managed relational databases
4. Lambda: Serverless computing

**Why AWS?**
- Scalability: Scale up or down based on demand
- Reliability: 99.99% uptime SLA
- Security: Enterprise-grade security features
- Global reach: Data centers worldwide

**Getting Started:**
Create an AWS account, explore the free tier, and start with simple services like S3 and EC2. Use the AWS CLI for automation.

**Best Practices:**
- Use IAM for access management
- Enable MFA for security
- Tag resources for cost tracking
- Implement auto-scaling
- Regular backups and disaster recovery

**Cost Optimization:**
Monitor usage, use reserved instances, leverage spot instances, and implement auto-scaling to optimize costs.""",
            "author": "James Wilson",
            "category": "Cloud Computing",
            "tags": ["AWS", "Cloud", "DevOps", "Tutorial"],
            "featured": True,
            "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=5),
            "updated_at": datetime.utcnow() - timedelta(days=5)
        },
        {
            "title": "Data Visualization with Python: Complete Guide",
            "content": """Data visualization is crucial for understanding and communicating insights. Learn how to create compelling visualizations with Python.

**Essential Libraries:**
1. Matplotlib: Foundation for plotting
2. Seaborn: Statistical visualizations
3. Plotly: Interactive plots
4. Pandas: Data manipulation and basic plots

**Types of Visualizations:**
- Line plots: Trends over time
- Bar charts: Categorical comparisons
- Scatter plots: Relationships between variables
- Heatmaps: Correlation matrices
- Box plots: Distribution analysis

**Best Practices:**
- Choose the right chart type
- Use appropriate color schemes
- Add clear labels and titles
- Keep it simple and clean
- Consider your audience

**Advanced Techniques:**
Create interactive dashboards with Plotly Dash, use Seaborn for statistical plots, and combine multiple visualizations for comprehensive analysis.""",
            "author": "Lisa Anderson",
            "category": "Data Science",
            "tags": ["Python", "Data Science", "Visualization", "Tutorial"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=6),
            "updated_at": datetime.utcnow() - timedelta(days=6)
        },
        {
            "title": "Modern JavaScript: ES2023 Features You Should Know",
            "content": """JavaScript continues to evolve. Let's explore the latest ES2023 features that make development more efficient and enjoyable.

**New Array Methods:**
- findLast(): Find elements from the end
- findLastIndex(): Get index from the end
- toReversed(): Non-mutating reverse
- toSorted(): Non-mutating sort
- toSpliced(): Non-mutating splice

**Hashbang Grammar:**
Directly executable JavaScript files with proper shebang support.

**Symbols as WeakMap Keys:**
Use symbols as keys in WeakMaps for better memory management.

**Why These Matter:**
- Improved code readability
- Better performance
- Enhanced functionality
- Cleaner APIs

**Adoption:**
Most modern browsers support ES2023 features. Use Babel for older browser compatibility.""",
            "author": "Alex Turner",
            "category": "Web Development",
            "tags": ["JavaScript", "Frontend", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=7),
            "updated_at": datetime.utcnow() - timedelta(days=7)
        },
        {
            "title": "Natural Language Processing: From Basics to BERT",
            "content": """Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language. Explore the journey from basics to state-of-the-art models.

**NLP Fundamentals:**
- Tokenization: Breaking text into words/tokens
- Stemming and Lemmatization: Word normalization
- POS Tagging: Identifying parts of speech
- Named Entity Recognition: Identifying entities

**Traditional Approaches:**
Bag of Words, TF-IDF, and Word2Vec laid the foundation for modern NLP.

**Transformer Revolution:**
Transformers changed NLP forever with attention mechanisms, enabling models to understand context better.

**BERT and Beyond:**
BERT (Bidirectional Encoder Representations from Transformers) set new benchmarks. Modern models like GPT and T5 continue advancing the field.

**Practical Applications:**
Sentiment analysis, chatbots, machine translation, text summarization, and question answering.""",
            "author": "Rachel Green",
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Deep Learning", "Tutorial"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1655720828018-edd2daec9349?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=8),
            "updated_at": datetime.utcnow() - timedelta(days=8)
        },
        {
            "title": "MongoDB Best Practices for Production",
            "content": """MongoDB is a powerful NoSQL database. Learn best practices for running MongoDB in production environments.

**Schema Design:**
- Embed related data when appropriate
- Use references for large or frequently changing data
- Design for your query patterns
- Consider data growth and access patterns

**Indexing:**
Create indexes on frequently queried fields, use compound indexes wisely, and monitor index usage with explain().

**Performance Optimization:**
- Use projection to limit returned fields
- Implement proper pagination
- Use aggregation pipeline efficiently
- Monitor slow queries

**Security:**
- Enable authentication
- Use role-based access control
- Encrypt data at rest and in transit
- Regular security audits

**Backup and Recovery:**
Implement automated backups, test restore procedures regularly, and consider point-in-time recovery options.

**Monitoring:**
Use MongoDB Atlas monitoring, set up alerts, track key metrics, and analyze query performance.""",
            "author": "Thomas Martinez",
            "category": "Data Science",
            "tags": ["MongoDB", "Data", "Best Practices", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=9),
            "updated_at": datetime.utcnow() - timedelta(days=9)
        },
        {
            "title": "Microservices Architecture: Design Patterns and Best Practices",
            "content": """Microservices architecture breaks down applications into small, independent services. Learn how to design and implement microservices effectively.

**Core Principles:**
1. Single Responsibility: Each service does one thing well
2. Autonomy: Services are independently deployable
3. Decentralization: Distributed decision making
4. Failure Isolation: Failures don't cascade

**Design Patterns:**
- API Gateway: Single entry point
- Service Discovery: Dynamic service location
- Circuit Breaker: Fault tolerance
- Event Sourcing: Audit trail and state management

**Communication:**
Use REST APIs for synchronous communication and message queues (RabbitMQ, Kafka) for asynchronous.

**Challenges:**
Distributed transactions, data consistency, monitoring, and debugging require careful planning.

**Tools:**
Docker for containerization, Kubernetes for orchestration, and service meshes like Istio for advanced features.""",
            "author": "Kevin Brown",
            "category": "Cloud Computing",
            "tags": ["DevOps", "Cloud", "Best Practices", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=10),
            "updated_at": datetime.utcnow() - timedelta(days=10)
        },
        {
            "title": "TypeScript for JavaScript Developers: A Practical Guide",
            "content": """TypeScript adds static typing to JavaScript, catching errors before runtime. Learn how to leverage TypeScript in your projects.

**Why TypeScript?**
- Catch errors during development
- Better IDE support and autocomplete
- Improved code documentation
- Easier refactoring

**Basic Types:**
```typescript
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let numbers: number[] = [1, 2, 3];
```

**Interfaces:**
Define object shapes for better type safety and documentation.

**Generics:**
Create reusable components that work with multiple types.

**Advanced Features:**
Union types, intersection types, type guards, and mapped types provide powerful type manipulation.

**Migration Strategy:**
Start by renaming .js to .ts files, add types gradually, enable strict mode incrementally, and leverage type inference.""",
            "author": "Jennifer Lee",
            "category": "Web Development",
            "tags": ["JavaScript", "Frontend", "Tutorial", "Beginner"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=11),
            "updated_at": datetime.utcnow() - timedelta(days=11)
        },
        {
            "title": "Computer Vision with OpenCV and Python",
            "content": """Computer vision enables machines to interpret visual information. Learn how to build computer vision applications with OpenCV.

**OpenCV Basics:**
OpenCV is the most popular computer vision library, offering tools for image processing, object detection, and more.

**Common Tasks:**
1. Image preprocessing: Resize, crop, filter
2. Edge detection: Canny, Sobel operators
3. Object detection: Haar cascades, YOLO
4. Face recognition: Deep learning models

**Implementation:**
```python
import cv2
image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

**Deep Learning Integration:**
Combine OpenCV with TensorFlow or PyTorch for advanced tasks like semantic segmentation and instance segmentation.

**Applications:**
Autonomous vehicles, facial recognition, medical imaging, augmented reality, and quality inspection.""",
            "author": "Daniel Park",
            "category": "AI/ML",
            "tags": ["AI", "Python", "Deep Learning", "Tutorial"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1535378620166-273708d44e4c?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=12),
            "updated_at": datetime.utcnow() - timedelta(days=12)
        },
        {
            "title": "RESTful API Design: Principles and Best Practices",
            "content": """REST (Representational State Transfer) is the standard for web APIs. Learn how to design clean, maintainable RESTful APIs.

**REST Principles:**
1. Client-Server: Separation of concerns
2. Stateless: Each request contains all necessary information
3. Cacheable: Responses indicate if they can be cached
4. Uniform Interface: Consistent API design

**URL Design:**
- Use nouns, not verbs: /users, not /getUsers
- Use plural names: /posts, not /post
- Nest resources logically: /users/123/posts
- Use query parameters for filtering and pagination

**HTTP Methods:**
- GET: Retrieve resources
- POST: Create resources
- PUT: Update entire resources
- PATCH: Partial updates
- DELETE: Remove resources

**Status Codes:**
Use appropriate HTTP status codes: 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Server Error).

**Versioning:**
Include version in URL (/api/v1/) or headers for backward compatibility.""",
            "author": "Maria Garcia",
            "category": "Web Development",
            "tags": ["Backend", "Best Practices", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=13),
            "updated_at": datetime.utcnow() - timedelta(days=13)
        },
        {
            "title": "Data Engineering: Building Robust Data Pipelines",
            "content": """Data engineering focuses on designing and building systems for collecting, storing, and analyzing data at scale.

**Key Responsibilities:**
- Design data architecture
- Build ETL/ELT pipelines
- Ensure data quality
- Optimize performance
- Maintain data infrastructure

**Essential Tools:**
1. Apache Airflow: Workflow orchestration
2. Apache Spark: Large-scale data processing
3. Kafka: Real-time data streaming
4. dbt: Data transformation

**Pipeline Design:**
Extract data from sources, transform it to the desired format, and load it into data warehouses or lakes.

**Best Practices:**
- Implement data validation
- Handle failures gracefully
- Monitor pipeline health
- Document data lineage
- Version control your pipelines

**Cloud Platforms:**
AWS (Glue, EMR), Google Cloud (Dataflow, BigQuery), Azure (Data Factory, Synapse).""",
            "author": "Christopher Davis",
            "category": "Data Science",
            "tags": ["Data", "Python", "Best Practices", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=14),
            "updated_at": datetime.utcnow() - timedelta(days=14)
        },
        {
            "title": "Kubernetes: Container Orchestration Simplified",
            "content": """Kubernetes automates deployment, scaling, and management of containerized applications. Master the basics of K8s.

**What is Kubernetes?**
An open-source platform for managing containerized workloads and services across clusters of machines.

**Core Concepts:**
1. Pods: Smallest deployable units
2. Services: Expose applications
3. Deployments: Manage pod replicas
4. ConfigMaps & Secrets: Configuration management
5. Ingress: HTTP routing

**Architecture:**
- Control Plane: Manages the cluster
- Nodes: Worker machines running containers
- etcd: Distributed key-value store

**Getting Started:**
Use Minikube for local development, kubectl for cluster management, and Helm for package management.

**Best Practices:**
- Use namespaces for organization
- Implement resource limits
- Set up health checks
- Use rolling updates
- Monitor with Prometheus

**When to Use:**
Kubernetes is ideal for microservices, cloud-native applications, and teams managing multiple containers.""",
            "author": "Andrew Thompson",
            "category": "Cloud Computing",
            "tags": ["DevOps", "Cloud", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=15),
            "updated_at": datetime.utcnow() - timedelta(days=15)
        },
        {
            "title": "GraphQL vs REST: Choosing the Right API Technology",
            "content": """GraphQL and REST are both popular API technologies. Understand their differences and when to use each.

**REST APIs:**
Strengths:
- Simple and well-understood
- Great caching support
- Wide tooling ecosystem
- Easy to implement

Weaknesses:
- Over-fetching and under-fetching
- Multiple endpoints
- Version management challenges

**GraphQL:**
Strengths:
- Request exactly what you need
- Single endpoint
- Strong typing
- Real-time updates with subscriptions

Weaknesses:
- Caching complexity
- Learning curve
- Query complexity management

**When to Use REST:**
- Simple CRUD operations
- Public APIs
- Caching is critical
- Team familiarity with REST

**When to Use GraphQL:**
- Complex data relationships
- Mobile applications (bandwidth concerns)
- Rapid iteration needed
- Multiple clients with different data needs

**Conclusion:**
Both have their place. Consider your specific requirements, team expertise, and use case.""",
            "author": "Nicole White",
            "category": "Web Development",
            "tags": ["Backend", "Tutorial", "Best Practices"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=16),
            "updated_at": datetime.utcnow() - timedelta(days=16)
        },
        {
            "title": "Reinforcement Learning: Teaching Machines Through Rewards",
            "content": """Reinforcement Learning (RL) teaches agents to make decisions through trial and error, receiving rewards or penalties.

**Core Components:**
1. Agent: The learner/decision maker
2. Environment: The world agent interacts with
3. State: Current situation
4. Action: What agent can do
5. Reward: Feedback signal

**Learning Process:**
The agent takes actions, receives rewards, and updates its strategy to maximize cumulative reward over time.

**Key Algorithms:**
- Q-Learning: Value-based method
- Deep Q-Networks (DQN): Deep learning + Q-Learning
- Policy Gradient: Direct policy optimization
- Actor-Critic: Combines value and policy methods

**Applications:**
Game playing (AlphaGo), robotics, autonomous vehicles, resource management, and recommendation systems.

**Getting Started:**
Use OpenAI Gym for environments, implement basic Q-Learning, then progress to deep RL with stable-baselines3 or RLlib.

**Challenges:**
Sample efficiency, reward design, exploration vs exploitation, and training stability.""",
            "author": "Brian Miller",
            "category": "AI/ML",
            "tags": ["AI", "Machine Learning", "Deep Learning", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=17),
            "updated_at": datetime.utcnow() - timedelta(days=17)
        },
        {
            "title": "Serverless Computing: The Future of Cloud Applications",
            "content": """Serverless computing lets you build applications without managing infrastructure. Focus on code, not servers.

**What is Serverless?**
A cloud execution model where the provider manages server allocation and scaling automatically.

**Benefits:**
- No server management
- Automatic scaling
- Pay per execution
- Faster time to market
- Built-in high availability

**Popular Platforms:**
1. AWS Lambda: Most mature platform
2. Google Cloud Functions: Great for GCP ecosystem
3. Azure Functions: Microsoft cloud integration
4. Cloudflare Workers: Edge computing

**Use Cases:**
- API backends
- Data processing
- Scheduled tasks
- Event-driven applications
- Webhooks

**Best Practices:**
- Keep functions small and focused
- Manage cold starts
- Use environment variables
- Implement proper error handling
- Monitor and log everything

**Limitations:**
Execution time limits, vendor lock-in, debugging challenges, and cold start latency.""",
            "author": "Stephanie Clark",
            "category": "Cloud Computing",
            "tags": ["Cloud", "DevOps", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1639322537228-f710d846310a?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=18),
            "updated_at": datetime.utcnow() - timedelta(days=18)
        },
        {
            "title": "Web Performance Optimization: Making Sites Lightning Fast",
            "content": """Website performance directly impacts user experience and SEO. Learn essential optimization techniques.

**Core Web Vitals:**
1. LCP (Largest Contentful Paint): Loading performance
2. FID (First Input Delay): Interactivity
3. CLS (Cumulative Layout Shift): Visual stability

**Optimization Strategies:**

**Images:**
- Use modern formats (WebP, AVIF)
- Implement lazy loading
- Serve responsive images
- Compress images

**JavaScript:**
- Code splitting
- Tree shaking
- Minification
- Defer non-critical JS

**CSS:**
- Critical CSS inline
- Remove unused CSS
- Minify CSS files

**Caching:**
- Browser caching
- CDN usage
- Service workers

**Measuring Performance:**
Use Lighthouse, WebPageTest, and Chrome DevTools to identify and fix bottlenecks.

**Best Practices:**
Optimize above-the-fold content, reduce HTTP requests, enable compression, and use a CDN.""",
            "author": "Robert Taylor",
            "category": "Web Development",
            "tags": ["Frontend", "Best Practices", "Tutorial", "Advanced"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=19),
            "updated_at": datetime.utcnow() - timedelta(days=19)
        },
        {
            "title": "Time Series Forecasting with Python and Prophet",
            "content": """Time series forecasting predicts future values based on historical data. Learn how to build accurate forecasting models with Prophet.

**What is Time Series?**
Data points collected at successive time intervals, like stock prices, weather, or sales data.

**Prophet Library:**
Developed by Facebook, Prophet makes time series forecasting accessible and robust.

**Key Features:**
- Handles missing data
- Detects outliers automatically
- Works with daily, weekly seasonality
- Supports holiday effects

**Implementation:**
```python
from prophet import Prophet
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)
```

**Components:**
- Trend: Long-term movement
- Seasonality: Periodic patterns
- Holidays: Special events
- Residuals: Random noise

**Applications:**
Sales forecasting, demand planning, resource allocation, and financial predictions.

**Best Practices:**
Validate with cross-validation, tune hyperparameters, and combine multiple models for better accuracy.""",
            "author": "Laura Martinez",
            "category": "Data Science",
            "tags": ["Python", "Data Science", "Machine Learning", "Tutorial"],
            "featured": False,
            "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800",
            "views": random.randint(100, 5000),
            "likes": random.randint(10, 500),
            "created_at": datetime.utcnow() - timedelta(days=20),
            "updated_at": datetime.utcnow() - timedelta(days=20)
        }
    ]
    
    blogs_collection.insert_many(blogs)
    print(f"Inserted {len(blogs)} blog posts")

def main():
    print("=== Starting Database Seed ===")
    clear_collections()
    seed_categories()
    seed_tags()
    seed_blogs()
    print("=== Seed completed successfully! ===")

if __name__ == "__main__":
    main()
