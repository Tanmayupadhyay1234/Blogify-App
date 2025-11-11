# 🚀 Blogify - AI-Powered Magazine Blog Platform

A modern, full-stack blog platform with AI-powered features, instant authentication, and a stunning magazine-style UI. Built with React, FastAPI, MongoDB, and GROQ AI.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![React](https://img.shields.io/badge/React-18.2.0-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb)

## ✨ Features

### 🎨 Frontend Features
- **Magazine-Style UI** - Modern, responsive design with card layouts and smooth animations
- **Hero Section** - Auto-rotating featured posts with stunning visuals
- **Trending Posts** - Sort by views, likes, or recency with real-time updates
- **Latest News** - 15 expandable news items with live updates
- **Category Browsing** - 10+ categories including Technology, AI/ML, Data Science, Web Development
- **Tag System** - Filter and discover related content
- **Search Functionality** - Full-text search across all blog posts
- **Dark/Light Mode** - Seamless theme switching
- **Responsive Design** - Mobile-first approach, works on all devices

### 🤖 AI Features
- **AI Chatbot** - Floating chatbot for Q&A about blog content
- **Content Summarization** - GROQ AI-powered blog summaries
- **Smart Recommendations** - Related posts based on categories and tags
- **AI-Generated Content** - 60+ blogs generated with GROQ AI

### 🔐 Authentication
- **Instant Login** - No password required, sign in as User or Admin
- **Role-Based Access** - Admin panel for content management
- **JWT Authentication** - Secure token-based auth

### 📊 Admin Features
- **Content Management** - Create, edit, and delete blog posts
- **Category Management** - Organize content by categories
- **Tag Management** - Add and manage tags
- **Featured Posts** - Mark posts as featured
- **Analytics** - View counts, likes, and engagement metrics

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern React with hooks
- **React Router v6** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client
- **React Context API** - State management
- **React Icons** - Icon library

### Backend
- **FastAPI** - High-performance Python web framework
- **PyMongo** - MongoDB driver
- **GROQ AI SDK** - AI-powered features
- **Pydantic** - Data validation
- **JWT** - Authentication tokens
- **Uvicorn** - ASGI server

### Database
- **MongoDB Atlas** - Cloud-hosted NoSQL database

### Deployment
- **Netlify** - Frontend hosting
- **Render/Railway** - Backend hosting options

## 📦 Installation & Setup

### Prerequisites
- Node.js 16+ and npm
- Python 3.9+
- MongoDB Atlas account
- GROQ API key (free at [groq.com](https://groq.com))

### 1. Clone Repository
```bash
git clone https://github.com/Tanmayupadhyay1234/Blogify-App.git
cd Blogify-App
```

### 2. Backend Setup

```bash
cd server

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env with your credentials:
# MONGODB_URI=your_mongodb_connection_string
# GROQ_API_KEY=your_groq_api_key
# SECRET_KEY=your-secret-key-here
# PORT=8000

# Seed database with AI-generated content
python ai_seed_data.py

# Start backend server
python main.py
```

Backend runs at: `http://localhost:8000`

### 3. Frontend Setup

```bash
cd client

# Install dependencies
npm install

# Create .env file
copy .env.example .env

# Edit .env:
# REACT_APP_API_URL=http://localhost:8000

# Start development server
npm start
```

Frontend runs at: `http://localhost:3000`

## 🌐 Deployment

### Deploy Frontend to Netlify

1. Push code to GitHub
2. Go to [netlify.com](https://netlify.com) and sign in
3. Click "Add new site" → "Import an existing project"
4. Connect your GitHub repository
5. Build settings (auto-detected from `netlify.toml`):
   - Base directory: `client`
   - Build command: `npm run build`
   - Publish directory: `client/build`
6. Add environment variable:
   - `REACT_APP_API_URL` = your backend URL
7. Deploy!

### Deploy Backend

**Option 1: Render**
1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect GitHub repository
4. Settings:
   - Root Directory: `server`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables from `.env.example`
6. Deploy!

**Option 2: Railway**
1. Go to [railway.app](https://railway.app)
2. Create new project from GitHub
3. Add environment variables
4. Deploy automatically

## 📁 Project Structure

```
Blogify/
├── client/                    # React frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   │   ├── BlogCard.jsx
│   │   │   ├── BlogChatInterface.jsx
│   │   │   ├── ChatBot.jsx
│   │   │   ├── ErrorBoundary.jsx
│   │   │   ├── FeaturedPosts.jsx
│   │   │   ├── FloatingChatWidget.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── HeroSection.jsx
│   │   │   ├── InfiniteScroll.jsx
│   │   │   ├── LatestNews.jsx
│   │   │   ├── LikeButton.jsx
│   │   │   ├── LoadingSpinner.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── ReadingTime.jsx
│   │   │   ├── ShareButtons.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Toast.jsx
│   │   │   ├── TopReads.jsx
│   │   │   └── TrendingSection.jsx
│   │   ├── context/          # React Context
│   │   │   ├── AuthContext.js
│   │   │   └── ThemeContext.js
│   │   ├── pages/            # Page components
│   │   │   ├── AdminDashboard.jsx
│   │   │   ├── BlogDetail.jsx
│   │   │   ├── CategoriesPage.jsx
│   │   │   ├── CategoryPage.jsx
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── SearchPage.jsx
│   │   │   └── TagPage.jsx
│   │   ├── services/         # API services
│   │   │   └── api.js
│   │   ├── App.js
│   │   ├── index.css
│   │   └── index.js
│   ├── .env.example
│   ├── package.json
│   ├── postcss.config.js
│   └── tailwind.config.js
│
├── server/                    # FastAPI backend
│   ├── main.py               # Entry point
│   ├── routes.py             # API routes
│   ├── models.py             # Pydantic models
│   ├── auth.py               # Authentication
│   ├── ai.py                 # AI features (GROQ)
│   ├── database.py           # MongoDB connection
│   ├── dependencies.py       # Auth dependencies
│   ├── ai_seed_data.py       # AI-powered data seeding
│   ├── seed_data.py          # Manual data seeding
│   ├── .env.example
│   └── requirements.txt
│
├── extras/                    # Non-essential files
│   ├── data.py
│   ├── milvus_service.py
│   ├── seed_data_new.py
│   └── url_test.py
│
├── .gitignore
├── netlify.toml              # Netlify config
└── README.md
```

## 🎯 Usage Guide

### For Users

1. **Browse Content**
   - Visit homepage to see featured posts and trending content
   - Click on any blog card to read full article
   - Use search bar to find specific topics

2. **Explore Categories**
   - Click "Categories" in navbar
   - Browse 10+ categories
   - Filter by Technology, AI/ML, Data Science, etc.

3. **Interact with Content**
   - Like posts with heart button
   - Share on social media
   - View reading time estimates
   - Check view counts

4. **AI Chat**
   - Click floating chat button on blog pages
   - Ask questions about the article
   - Get instant AI-powered answers

5. **Latest News**
   - Scroll to news section on homepage
   - Click any news item to expand
   - View all 15 latest news updates

### For Admins

1. **Login as Admin**
   - Go to `/login`
   - Toggle "Admin" role
   - Click "Sign In"

2. **Create Posts**
   - Navigate to `/admin`
   - Click "Create New Post"
   - Fill in title, content, category, tags
   - Add image URL
   - Mark as featured (optional)
   - Submit

3. **Manage Content**
   - View all posts in admin dashboard
   - Edit or delete existing posts
   - Monitor engagement metrics

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/login` - Instant login

### Blogs
- `GET /api/blogs` - Get all blogs (paginated)
- `GET /api/blogs/featured` - Get featured blogs
- `GET /api/blogs/trending` - Get trending blogs
- `GET /api/blogs/{id}` - Get single blog
- `POST /api/blogs` - Create blog (admin)
- `PUT /api/blogs/{id}` - Update blog (admin)
- `DELETE /api/blogs/{id}` - Delete blog (admin)
- `GET /api/blogs/{id}/related` - Get related blogs

### Categories & Tags
- `GET /api/categories` - Get all categories
- `GET /api/categories/{name}/posts` - Get posts by category
- `GET /api/tags` - Get all tags
- `GET /api/tags/{name}/posts` - Get posts by tag

### Search
- `GET /api/search?q={query}` - Search blogs

### AI Features
- `POST /api/ai/summarize` - Summarize blog
- `POST /api/ai/chat` - Chat with AI about blog

### News
- `GET /api/latest-news` - Get latest news

**Full API Documentation:** Visit `http://localhost:8000/docs` when backend is running

## 🎨 UI Features

### Hero Section
- Auto-rotating featured posts (5-second intervals)
- Full-screen hero with gradient overlay
- Category badges and metadata
- Call-to-action button
- Navigation indicators

### Trending Section
- Sort by Most Viewed, Most Liked, or Recent
- 4-column responsive grid
- Hover effects with image zoom
- View and like counts
- Category badges

### Latest News
- 15 expandable news items
- 3-column responsive grid
- Click to expand/collapse
- Live badge with pulse animation
- Category tags and timestamps

### Blog Detail Page
- Full-width hero image
- Author avatar and metadata
- Reading time calculation
- Like and share buttons
- View counter
- Related posts section
- Floating AI chat widget

## 🔧 Configuration

### Environment Variables

**Backend (.env)**
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
GROQ_API_KEY=gsk_xxxxxxxxxxxxx
SECRET_KEY=your-secret-key-minimum-32-characters
PORT=8000
```

**Frontend (.env)**
```env
REACT_APP_API_URL=http://localhost:8000
```

### MongoDB Collections
- `blog_posts` - Blog articles
- `categories` - Blog categories
- `tags` - Blog tags
- `users` - User accounts
- `comments` - Blog comments (future)
- `latest_news` - News items

## 🚀 Performance

- **Lazy Loading** - Images load on scroll
- **Code Splitting** - React lazy loading
- **Caching** - Browser and API caching
- **Optimized Images** - Unsplash CDN
- **Fast API** - FastAPI performance
- **MongoDB Indexing** - Optimized queries

## 🔒 Security

- **JWT Authentication** - Secure tokens
- **CORS Protection** - Configured origins
- **Input Validation** - Pydantic models
- **Environment Variables** - Secrets management
- **Role-Based Access** - Admin protection
- **Secret Scanning** - GitHub protection

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

MIT License - see LICENSE file for details

## 👨‍💻 Author

**Tanmay Upadhyay**
- GitHub: [@Tanmayupadhyay1234](https://github.com/Tanmayupadhyay1234)
- Repository: [Blogify-App](https://github.com/Tanmayupadhyay1234/Blogify-App)

## 🙏 Acknowledgments

- [GROQ AI](https://groq.com) - AI-powered features
- [Unsplash](https://unsplash.com) - High-quality images
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - Database hosting
- [Netlify](https://netlify.com) - Frontend hosting
- [FastAPI](https://fastapi.tiangolo.com) - Backend framework
- [React](https://react.dev) - Frontend framework

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Email: support@blogify.com (if available)

## 🗺️ Roadmap

- [ ] User profiles and avatars
- [ ] Comment system with nested replies
- [ ] Bookmark/save posts
- [ ] Email notifications
- [ ] Social media integration
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Progressive Web App (PWA)
- [ ] RSS feed
- [ ] Newsletter subscription

---

**Made with ❤️ by Tanmay Upadhyay**

⭐ Star this repo if you find it helpful!
