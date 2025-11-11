# 🚀 Quick Start Guide - Blogify

## Prerequisites
- Node.js 16+ and npm
- Python 3.9+
- MongoDB Atlas account (free tier)
- GROQ API key (free from https://console.groq.com)

---

## 🔧 Setup (5 minutes)

### 1. Backend Setup

```bash
# Navigate to server directory
cd server

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
```

Create `server/.env`:
```env
MONGODB_URI=your_mongodb_atlas_connection_string
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your-secret-key-change-this
PORT=5010
```

```bash
# Seed database with sample data
python seed_data.py

# Start backend server
uvicorn main:app --host 0.0.0.0 --port 5010 --reload
```

Backend runs at: **http://localhost:5010**

---

### 2. Frontend Setup

```bash
# Navigate to client directory (new terminal)
cd client

# Install dependencies
npm install

# Create .env file
```

Create `client/.env`:
```env
REACT_APP_API_URL=http://localhost:5010
```

```bash
# Start frontend
npm start
```

Frontend runs at: **http://localhost:3000**

---

## ✅ Test the App

1. **Open browser**: http://localhost:3000
2. **Login**: Click "Login" → Enter username → Select role → Sign In
3. **Browse blogs**: View featured posts, trending articles
4. **Read article**: Click any blog → See split-view with AI chatbot
5. **Chat with AI**: Ask questions about the article on the right panel
6. **Admin features** (if logged in as admin):
   - Go to `/admin`
   - Create/Edit/Delete blog posts

---

## 🎯 Key Features to Try

- ✅ **Split-view reading**: Blog on left, AI chat on right
- ✅ **Dark mode**: Toggle in navbar
- ✅ **Search**: Type in navbar, see autocomplete
- ✅ **Categories**: Browse 14 different categories
- ✅ **Trending**: View most popular posts
- ✅ **AI Chat**: Ask questions about any article
- ✅ **Social**: Like and share posts

---

## 🐛 Troubleshooting

**Backend won't start:**
- Check MongoDB URI is correct
- Verify GROQ API key is valid
- Ensure port 5010 is not in use

**Frontend won't start:**
- Run `npm install` again
- Check backend is running on port 5010
- Clear browser cache

**AI chat not working:**
- Verify GROQ_API_KEY in server/.env
- Check backend console for errors
- Ensure backend is running

---

## 📝 Default Credentials

**Instant Login** - No password required!
- Username: Any name (or leave blank)
- Role: User or Admin

---

## 🎉 You're Ready!

Enjoy your AI-powered blog platform with split-view reading experience!
