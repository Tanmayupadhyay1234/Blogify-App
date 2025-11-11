# Blogify Setup Guide

## UI/UX Improvements Made

### 1. **Toast Notifications**
- Added global toast notification system for user feedback
- Success, error, and info messages
- Auto-dismiss after 4 seconds

### 2. **Dark Mode Support**
- Fixed all components to respect dark/light theme
- Consistent color variables across the app
- Smooth transitions between themes

### 3. **Error Handling**
- Added ErrorBoundary for graceful error handling
- Toast notifications for API errors
- Better user feedback on failures

### 4. **Loading States**
- Created LoadingSpinner component
- Consistent loading indicators across pages
- Better UX during data fetching

### 5. **API Configuration**
- Fixed port mismatch (backend now runs on 5010)
- Consistent API URLs across frontend and backend

## Setup Instructions

### Backend Setup

1. Navigate to server directory:
```bash
cd server
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
MONGODB_URI=your_mongodb_atlas_connection_string
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your-secret-key-change-this
PORT=5010
```

5. Seed database:
```bash
python ai_seed_data.py
```

6. Start server:
```bash
python main.py
```

Backend runs at: `http://localhost:5010`

### Frontend Setup

1. Navigate to client directory:
```bash
cd client
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file:
```env
REACT_APP_API_URL=http://localhost:5010
```

4. Start development server:
```bash
npm start
```

Frontend runs at: `http://localhost:3000`

## Key Features

### User Experience
- ✅ Instant login (no password required)
- ✅ Dark/Light mode toggle
- ✅ Toast notifications for all actions
- ✅ Loading spinners during data fetch
- ✅ Error boundaries for crash prevention
- ✅ Responsive design
- ✅ Smooth animations and transitions

### Admin Features
- ✅ Create/Edit/Delete blog posts
- ✅ Toast feedback for all operations
- ✅ Dark mode support in admin panel
- ✅ Form validation

### AI Features
- ✅ AI-powered chatbot
- ✅ Context-aware responses
- ✅ Error handling with user feedback

## Testing the Flow

1. **Login Flow**
   - Go to `/login`
   - Enter username (optional)
   - Select role (User/Admin)
   - Click "Sign In"
   - See success toast notification
   - Redirected to home page

2. **Browse Blogs**
   - View featured posts on home page
   - Click on any blog to read full article
   - See related posts at bottom
   - Like and share functionality

3. **Admin Flow** (Login as Admin)
   - Go to `/admin`
   - Create new blog post
   - See success toast
   - View/Delete existing posts
   - All actions show toast feedback

4. **AI Chatbot**
   - Click chatbot icon (bottom right)
   - Ask questions about blogs
   - Get AI-powered responses
   - Error handling if API fails

5. **Search & Filter**
   - Use search bar in navbar
   - See live suggestions
   - Filter by category or tag
   - Responsive results

## Troubleshooting

### Backend Issues
- **Port 5010 in use**: Change PORT in `.env`
- **MongoDB connection failed**: Check MONGODB_URI
- **GROQ API error**: Verify GROQ_API_KEY

### Frontend Issues
- **API connection error**: Ensure backend is running on port 5010
- **Toast not showing**: Check browser console for errors
- **Dark mode not working**: Clear browser cache

## Next Steps

1. Run `npm install` in client directory to install Tailwind CSS
2. Start backend server
3. Start frontend server
4. Test all features
5. Enjoy the improved UI/UX!
