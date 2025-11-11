# Magazine-Style Blog Platform

## Overview
A full-stack blog platform with AI-powered features, built with React and FastAPI. The platform features instant authentication, category-based organization, GROQ AI integration for content summarization, and a magazine-style UI inspired by Analytics India Magazine and MachineHack.

## Project Structure
- **client/** - React frontend (runs on localhost:3000)
- **server/** - FastAPI backend (runs on localhost:5010)

## Tech Stack
### Frontend
- React with Hooks and Context API
- React Router for navigation
- Tailwind CSS for styling
- Axios for API communication

### Backend
- FastAPI (Python)
- PyMongo for MongoDB Atlas
- GROQ AI for content summarization
- Pydantic for data validation

### Database
- MongoDB Atlas (cloud-hosted)
- Collections: users, blog_posts, categories, tags

## Key Features
1. **Instant Login** - Username/password fields present but sign-in works without validation
2. **Admin/User Toggle** - Switch between roles with different permissions
3. **GROQ AI Integration** - Blog summarization and Q&A functionality
4. **Category & Tag System** - Organized content browsing
5. **Search Functionality** - Full-text search across blog posts
6. **Related Posts** - Category and tag-based recommendations
7. **Magazine-Style UI** - Featured posts, card layouts, responsive design
8. **Infinite Scroll** - Pagination for blog lists

## Local Development Setup
1. Install backend dependencies: `cd server && pip install -r requirements.txt`
2. Install frontend dependencies: `cd client && npm install`
3. Copy environment files and configure API keys
4. Run backend: `cd server && uvicorn main:app --host 0.0.0.0 --port 5010 --reload`
5. Run frontend: `cd client && npm start` (port 3000)

## API Endpoints
- `/api/auth/login` - Instant login (admin/user)
- `/api/blogs` - Get all blogs (with pagination)
- `/api/blogs/{id}` - Get single blog
- `/api/blogs/featured` - Get featured posts
- `/api/blogs/{id}/related` - Get related posts
- `/api/categories` - Get all categories
- `/api/tags` - Get all tags
- `/api/search?q=term` - Search blogs
- `/api/ai/summarize` - GROQ AI summarization

## Environment Configuration
### Backend (server/.env)
- MONGODB_URI - MongoDB Atlas connection string
- GROQ_API_KEY - GROQ AI API key
- SECRET_KEY - JWT secret for authentication
- PORT - Backend server port (5010)

### Frontend (client/.env)
- REACT_APP_API_URL - Backend API URL (http://localhost:5010)

## User Preferences
- Designed for local development with downloadable project
- Frontend runs on port 3000, backend on port 5010
- Instant authentication without password validation
- Magazine-style responsive UI

## Recent Changes
- **November 2025** - Security hardening complete:
  - Implemented JWT-based authentication with signed tokens
  - Made SECRET_KEY mandatory on startup (prevents forgeable tokens)
  - Protected all admin endpoints (blogs, categories, tags CRUD) with JWT verification
  - Created Admin Dashboard with blog creation/deletion functionality
  - Added Admin Dashboard link in navbar for admin users
  - Final security review passed by architect
- **January 2025** - Initial implementation:
  - Complete backend and frontend implementation
  - Seed data with 20+ sample blog posts
  - GROQ AI integration for summarization
  - Instant login with admin/user toggle

## Security Architecture
- **Authentication**: JWT tokens with HS256 signing algorithm
- **Authorization**: Role-based access control (RBAC) with server-side verification
- **Admin Protection**: All write operations (create/update/delete) require valid admin JWT
- **Public Access**: All read operations remain publicly accessible
- **Secret Management**: SECRET_KEY must be set in environment variables - app refuses to start without it
