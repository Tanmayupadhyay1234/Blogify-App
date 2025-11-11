# 🚀 Blogify - AI-Powered Magazine Blog Platform

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![React](https://img.shields.io/badge/React-18.2.0-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)
![Node](https://img.shields.io/badge/Node.js-16+-339933?logo=node.js)

**A modern, full-stack blog platform with AI-powered features, instant authentication, and a stunning magazine-style UI.**

[Live Demo](#) · [Documentation](#-installation--setup) · [Report Bug](https://github.com/Tanmayupadhyay1234/Blogify-App/issues) · [Request Feature](https://github.com/Tanmayupadhyay1234/Blogify-App/issues)

</div>

---

## 📑 Table of Contents

- [About The Project](#-about-the-project)
- [Screenshots](#-screenshots)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Installation](#-installation--setup)
- [Usage](#-usage-guide)
- [API Documentation](#-api-endpoints)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 About The Project

Blogify is a sophisticated, production-ready blog platform that combines modern web technologies with artificial intelligence to deliver an exceptional content management and reading experience. Built with React and FastAPI, it features a magazine-style interface, real-time AI chatbot assistance, and comprehensive content management capabilities.

> **🎯 Development Note**: This project was developed using **Vibe Coding** methodology with **Replit AI** for rapid prototyping and initial implementation. The project structure and core functionality were built through AI-assisted development, demonstrating modern collaborative coding practices.

### Why Blogify?

- **🤖 AI-Powered**: Integrated GROQ AI for content summarization and intelligent Q&A
- **⚡ Lightning Fast**: Built on FastAPI and React for optimal performance
- **🎨 Beautiful UI**: Magazine-style design with smooth animations and transitions
- **🔒 Secure**: JWT authentication with role-based access control
- **📱 Responsive**: Mobile-first design that works on all devices
- **🚀 Production Ready**: Fully deployable to Netlify, Render, or Railway

---

## 📸 Screenshots

### 🏠 Homepage - Magazine-Style Layout
![Homepage](Images/Homepage.png)
*Modern hero section with auto-rotating featured posts and trending content*

### 📈 Trending Blogs Section
![Trending Blogs](Images/Trending%20Blogs.png)
*Sort by views, likes, or recency with real-time updates*

### 📰 Latest News - 15 Expandable Items
![Latest News](Images/Latest%20News%20Section.png)
*Click any news item to expand and read full details*

### 📝 Blog Post Detail Page
![Blog Post](Images/Blog%20Post1.png)
*Full-width hero image with author metadata and reading time*

![Blog Post Complete](Images/Blog%20Post%201%20complete.png)
*Complete article view with related posts and AI chat widget*

### 🤖 AI-Powered Chatbot
![AI Chatbot](Images/AI%20Integrated%20chatbot.png)
*Floating AI assistant for instant Q&A about blog content*

![AI Chatbot Interface](Images/AI%20Integrated%20chatbot1.png)
*Intelligent responses powered by GROQ AI*

### 📂 Blog Categories
![Categories](Images/Blog%20Categories.png)
*Browse 10+ categories including Technology, AI/ML, Data Science*

### 🎛️ Admin Dashboard
![Admin Dashboard](Images/Admin%20Dashboard.png)
*Comprehensive content management system for admins*

### ✍️ Create Blog Post
![Adding Blog](Images/Adding%20a%20blog%20post.png)
*Intuitive interface for creating and managing blog posts*

### 🔐 Instant Login
![Login](Images/Login%20%20Page.png)
*No password required - instant authentication as User or Admin*

---

## ✨ Key Features

### 🎨 Frontend Excellence
- **Magazine-Style UI** - Professional, modern design with card-based layouts
- **Hero Section** - Auto-rotating featured posts every 5 seconds with smooth transitions
- **Trending Posts** - Dynamic sorting by views, likes, or recency
- **Latest News** - 15 expandable news items with live updates and pulse animations
- **Advanced Search** - Full-text search across all blog posts with instant suggestions
- **Category System** - 10+ categories (Technology, AI/ML, Data Science, Web Dev, Cloud, etc.)
- **Tag Filtering** - Discover related content through intelligent tagging
- **Dark/Light Mode** - Seamless theme switching with smooth transitions
- **Responsive Design** - Mobile-first approach, optimized for all screen sizes
- **Infinite Scroll** - Smooth content loading as you browse
- **Reading Time** - Automatic calculation of estimated reading time
- **Social Sharing** - Share posts on Twitter, LinkedIn, or copy link

### 🤖 AI-Powered Features
- **Intelligent Chatbot** - Floating AI assistant on every blog post
- **Context-Aware Q&A** - Ask questions about specific articles
- **Content Summarization** - GROQ AI-powered blog summaries
- **Smart Recommendations** - Related posts based on categories and tags
- **AI-Generated Content** - 60+ high-quality blogs generated with GROQ AI
- **Natural Language Processing** - Understanding user queries in natural language

### 🔐 Authentication & Security
- **Instant Login** - No password required for quick access
- **Role-Based Access Control** - User and Admin roles with different permissions
- **JWT Authentication** - Secure token-based authentication
- **Protected Routes** - Admin-only access to management features
- **Session Management** - Persistent login across browser sessions
- **CORS Protection** - Configured for secure cross-origin requests

### 🎛️ Admin Capabilities
- **Content Management System** - Full CRUD operations for blog posts
- **Category Management** - Create and organize content categories
- **Tag Management** - Add and manage content tags
- **Featured Posts** - Mark important posts as featured
- **Analytics Dashboard** - View counts, likes, and engagement metrics
- **Bulk Operations** - Manage multiple posts efficiently
- **Image Management** - Unsplash integration for high-quality images

### 👥 User Experience
- **Engagement Metrics** - Like buttons and view counters
- **Comment System** - (Coming soon) Nested comments with replies
- **Bookmarking** - (Coming soon) Save favorite posts
- **User Profiles** - (Coming soon) Personalized user pages
- **Notifications** - (Coming soon) Real-time updates

---

## 🛠️ Tech Stack

### Frontend Technologies
| Technology | Purpose | Version |
|-----------|---------|---------|
| **React** | UI Framework | 18.2.0 |
| **React Router** | Client-side routing | 6.20.0 |
| **Tailwind CSS** | Styling framework | 3.4.0 |
| **Axios** | HTTP client | 1.6.2 |
| **React Context API** | State management | Built-in |
| **React Icons** | Icon library | 4.12.0 |
| **React Quill** | Rich text editor | 2.0.0 |

### Backend Technologies
| Technology | Purpose | Version |
|-----------|---------|---------|
| **FastAPI** | Web framework | Latest |
| **PyMongo** | MongoDB driver | Latest |
| **GROQ AI SDK** | AI integration | Latest |
| **Pydantic** | Data validation | Latest |
| **Python-Jose** | JWT handling | Latest |
| **Uvicorn** | ASGI server | Latest |

### Database & Storage
- **MongoDB Atlas** - Cloud-hosted NoSQL database
- **Collections**: blog_posts, categories, tags, users, latest_news

### AI & Machine Learning
- **GROQ AI** - Fast AI inference for chatbot and summarization
- **LLaMA 3.1** - 8B instant model for natural language processing

### Deployment & DevOps
- **Netlify** - Frontend hosting with automatic deployments
- **Render/Railway** - Backend hosting options
- **GitHub Actions** - CI/CD pipeline (optional)
- **Docker** - Containerization (optional)

### Development Tools
- **Replit** - Initial development and prototyping environment
- **Vibe Coding** - AI-assisted development methodology

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.9 or higher) - [Download](https://python.org/)
- **Git** - [Download](https://git-scm.com/)
- **MongoDB Atlas Account** - [Sign up](https://www.mongodb.com/cloud/atlas)
- **GROQ API Key** - [Get free key](https://groq.com/)

### Quick Start (5 minutes)

```bash
# Clone the repository
git clone https://github.com/Tanmayupadhyay1234/Blogify-App.git
cd Blogify-App

# Setup backend
cd server
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
copy .env.example .env  # Edit with your credentials
python ai_seed_data.py  # Seed database
python main.py  # Start backend

# Setup frontend (new terminal)
cd client
npm install
copy .env.example .env  # Edit with backend URL
npm start  # Start frontend
```

Visit `http://localhost:3000` to see your blog platform! 🎉

---

## 📦 Installation & Setup

### Detailed Installation Guide

#### Step 1: Clone the Repository

```bash
git clone https://github.com/Tanmayupadhyay1234/Blogify-App.git
cd Blogify-App
```

#### Step 2: Backend Setup

```bash
cd server

# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux
```

**Configure `.env` file:**
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/blogify
GROQ_API_KEY=gsk_your_groq_api_key_here
SECRET_KEY=your-super-secret-key-min-32-chars
PORT=8000
```

**Seed the database with AI-generated content:**
```bash
python ai_seed_data.py
```

This will create:
- 60+ AI-generated blog posts
- 10+ categories
- 30+ tags
- 15 latest news items
- Sample users

**Start the backend server:**
```bash
python main.py
```

Backend will run at: `http://localhost:8000`
API docs available at: `http://localhost:8000/docs`

#### Step 3: Frontend Setup

Open a new terminal:

```bash
cd client

# Install dependencies
npm install

# Create environment file
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux
```

**Configure `.env` file:**
```env
REACT_APP_API_URL=http://localhost:8000
```

**Start the development server:**
```bash
npm start
```

Frontend will run at: `http://localhost:3000`

---

## 📖 Usage Guide

### For Regular Users

#### 1. Browsing Content
- **Homepage**: View featured posts in the hero section
- **Trending**: Sort posts by views, likes, or recency
- **Categories**: Browse 10+ categories from the navbar
- **Search**: Use the search bar for instant results
- **Tags**: Click on tags to find related content

#### 2. Reading Articles
- Click any blog card to read the full article
- View reading time estimate
- See author information and publish date
- Check view counts and engagement metrics
- Like posts with the heart button
- Share on social media platforms

#### 3. AI Chat Assistant
- Click the floating chat button on any blog post
- Ask questions about the article content
- Get instant AI-powered responses
- Reset conversation anytime

#### 4. Latest News
- Scroll to the news section on homepage
- Click any news item to expand and read full details
- View 15 latest news updates with timestamps

### For Administrators

#### 1. Admin Login
```
1. Navigate to /login
2. Enter username (optional)
3. Toggle "Admin" role
4. Click "Sign In"
```

#### 2. Creating Blog Posts
```
1. Go to /admin dashboard
2. Click "Create New Post"
3. Fill in the form:
    - Title (required)
    - Content (required)
    - Author name
    - Category (select from dropdown)
    - Tags (comma-separated)
    - Image URL (Unsplash recommended)
    - Featured checkbox (optional)
4. Click "Create Post"
```

#### 3. Managing Content
- **View All Posts**: See complete list in admin dashboard
- **Edit Posts**: Click "Edit" button on any post
- **Delete Posts**: Click "Delete" with confirmation
- **Monitor Analytics**: View engagement metrics

---

## 🔌 API Endpoints

### Authentication Endpoints
```http
POST /api/auth/login
```
**Request Body:**
```json
{
    "username": "user123",
    "role": "user" | "admin"
}
```

### Blog Endpoints
```http
GET     /api/blogs?page=1&limit=10                  # Get paginated blogs
GET     /api/blogs/featured                         # Get featured blogs
GET     /api/blogs/trending?limit=10                # Get trending blogs
GET     /api/blogs/{id}                             # Get single blog
POST    /api/blogs                                  # Create blog (admin only)
PUT     /api/blogs/{id}                             # Update blog (admin only)
DELETE  /api/blogs/{id}                             # Delete blog (admin only)
GET     /api/blogs/{id}/related                     # Get related blogs
```

### Category & Tag Endpoints
```http
GET /api/categories                                 # Get all categories
GET /api/categories/{name}/posts                    # Get posts by category
GET /api/tags                                       # Get all tags
GET /api/tags/{name}/posts                          # Get posts by tag
```

### Search Endpoint
```http
GET /api/search?q={query}                           # Search blogs
```

### AI Endpoints
```http
POST /api/ai/summarize                              # Summarize blog
POST /api/ai/chat                                   # Chat with AI
```

**Request Body for Chat:**
```json
{
    "query": "What is this article about?",
    "blog_id": "blog_id_here"
}
```

### News Endpoint
```http
GET /api/latest-news?limit=15                       # Get latest news
```

**Interactive API Documentation**: Visit `http://localhost:8000/docs` for Swagger UI

---

## 🌐 Deployment

### Deploy Frontend to Netlify

#### Method 1: Through Netlify Dashboard

1. **Push to GitHub**
    ```bash
    git add .
    git commit -m "Ready for deployment"
    git push origin main
    ```

2. **Connect to Netlify**
    - Go to [netlify.com](https://netlify.com)
    - Click "Add new site" → "Import an existing project"
    - Connect your GitHub account
    - Select `Blogify-App` repository

3. **Configure Build Settings**
    - Build settings are auto-detected from `netlify.toml`
    - Base directory: `client`
    - Build command: `npm run build`
    - Publish directory: `client/build`

4. **Add Environment Variables**
    - Go to Site settings → Environment variables
    - Add: `REACT_APP_API_URL` = `your_backend_url`

5. **Deploy**
    - Click "Deploy site"
    - Wait for build to complete
    - Your site is live! 🎉

#### Method 2: Netlify CLI

```bash
npm install -g netlify-cli
cd client
netlify login
netlify init
netlify deploy --prod
```

### Deploy Backend

#### Option 1: Render

1. **Create Account**
    - Go to [render.com](https://render.com)
    - Sign up with GitHub

2. **Create Web Service**
    - Click "New" → "Web Service"
    - Connect your repository
    - Select `Blogify-App`

3. **Configure Service**
    ```
    Name: blogify-backend
    Root Directory: server
    Environment: Python 3
    Build Command: pip install -r requirements.txt
    Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

4. **Add Environment Variables**
    ```
    MONGODB_URI=your_mongodb_uri
    GROQ_API_KEY=your_groq_key
    SECRET_KEY=your_secret_key
    PORT=8000
    ```

5. **Deploy**
    - Click "Create Web Service"
    - Wait for deployment
    - Copy the service URL

#### Option 2: Railway

1. **Create Account**
    - Go to [railway.app](https://railway.app)
    - Sign in with GitHub

2. **New Project**
    - Click "New Project"
    - Select "Deploy from GitHub repo"
    - Choose `Blogify-App`

3. **Configure**
    - Railway auto-detects Python
    - Add environment variables
    - Deploy automatically

4. **Get URL**
    - Copy the generated URL
    - Update frontend `REACT_APP_API_URL`

---

## 📁 Project Structure

> **Note**: Initial project structure and compilation phase completed using Vibe Coding with Replit AI.

```
Blogify/
│
├── client/                                         # React Frontend Application
│   ├── public/
│   │   └── index.html                              # HTML template
│   │
│   └── src/
│       ├── components/                             # Reusable React Components
│       │   ├── BlogCard.jsx                        # Blog post card component
│       │   ├── BlogChatInterface.jsx               # AI chat interface
│       │   ├── ChatBot.jsx                         # Floating chatbot widget
│       │   ├── ErrorBoundary.jsx                   # Error handling component
│       │   ├── FeaturedPosts.jsx                   # Featured posts section
│       │   ├── FloatingChatWidget.jsx              # Chat widget wrapper
│       │   ├── Footer.jsx                          # Site footer
│       │   ├── HeroSection.jsx                     # Homepage hero
│       │   ├── InfiniteScroll.jsx                  # Infinite scroll handler
│       │   ├── LatestNews.jsx                      # News section
│       │   ├── LikeButton.jsx                      # Like functionality
│       │   ├── LoadingSpinner.jsx                  # Loading indicator
│       │   ├── Navbar.jsx                          # Navigation bar
│       │   ├── ReadingTime.jsx                     # Reading time calculator
│       │   ├── ShareButtons.jsx                    # Social sharing
│       │   ├── Sidebar.jsx                         # Sidebar component
│       │   ├── Toast.jsx                           # Toast notifications
│       │   ├── TopReads.jsx                        # Top reads section
│       │   └── TrendingSection.jsx                 # Trending posts
│       │
│       ├── context/                                # React Context API
│       │   ├── AuthContext.js                      # Authentication state
│       │   └── ThemeContext.js                     # Theme management
│       │
│       ├── pages/                                  # Page Components
│       │   ├── AdminDashboard.jsx                  # Admin panel
│       │   ├── BlogDetail.jsx                      # Single blog view
│       │   ├── CategoriesPage.jsx                  # All categories
│       │   ├── CategoryPage.jsx                    # Category posts
│       │   ├── Home.jsx                            # Homepage
│       │   ├── Login.jsx                           # Login page
│       │   ├── SearchPage.jsx                      # Search results
│       │   └── TagPage.jsx                         # Tag posts
│       │
│       ├── services/                               # API Services
│       │   └── api.js                              # Axios API calls
│       │
│       ├── App.js                                  # Main App component
│       ├── index.css                               # Global styles
│       └── index.js                                # React entry point
│
├── server/                                         # FastAPI Backend Application
│   ├── main.py                                     # Application entry point
│   ├── routes.py                                   # API route definitions
│   ├── models.py                                   # Pydantic data models
│   ├── auth.py                                     # Authentication logic
│   ├── ai.py                                       # GROQ AI integration
│   ├── database.py                                 # MongoDB connection
│   ├── dependencies.py                             # Auth dependencies
│   ├── ai_seed_data.py                             # AI-powered seeding
│   ├── seed_data.py                                # Manual data seeding
│   ├── .env.example                                # Environment template
│   └── requirements.txt                            # Python dependencies
│
├── Images/                                         # Screenshot assets
│   ├── Homepage.png
│   ├── Trending Blogs.png
│   ├── Latest News Section.png
│   ├── Blog Post1.png
│   ├── Blog Post 1 complete.png
│   ├── AI Integrated chatbot.png
│   ├── AI Integrated chatbot1.png
│   ├── Blog Categories.png
│   ├── Admin Dashboard.png
│   ├── Adding a blog post.png
│   └── Login  Page.png
│
├── extras/                                         # Non-essential files
│   ├── data.py                                     # Legacy data file
│   ├── milvus_service.py                           # Vector DB service
│   ├── seed_data_new.py                            # Alternative seeding
│   └── url_test.py                                 # URL testing script
│
├── .gitignore                                      # Git ignore rules
├── netlify.toml                                    # Netlify configuration
└── README.md                                       # This file
```

---

## 🔮 Future Enhancements

- [ ] **Comment System** - Nested comments with replies and reactions
- [ ] **User Profiles** - Personalized user pages with activity history
- [ ] **Bookmarking** - Save and organize favorite posts
- [ ] **Email Notifications** - Subscribe to new posts and updates
- [ ] **Advanced Analytics** - Detailed engagement metrics and insights
- [ ] **Multi-language Support** - Internationalization (i18n)
- [ ] **Progressive Web App** - Offline support and installability
- [ ] **Rich Media Support** - Video and audio content embedding
- [ ] **SEO Optimization** - Enhanced meta tags and structured data
- [ ] **Social Login** - OAuth integration (Google, GitHub, Twitter)
- [ ] **Content Scheduling** - Schedule posts for future publication
- [ ] **Draft System** - Save and edit drafts before publishing
- [ ] **Version Control** - Track post revisions and changes
- [ ] **Advanced Search** - Filters, facets, and fuzzy matching
- [ ] **Newsletter Integration** - Email subscription and campaigns

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow the existing code style and conventions
- Write clear, descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 📧 Contact

**Tanmay Upadhyay**

- GitHub: [@Tanmayupadhyay1234](https://github.com/Tanmayupadhyay1234)
- Project Link: [https://github.com/Tanmayupadhyay1234/Blogify-App](https://github.com/Tanmayupadhyay1234/Blogify-App)

---

<div align="center">

**Made with ❤️ by Tanmay Upadhyay**

⭐ Star this repo if you find it helpful!

</div>
