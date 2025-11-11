import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useToast } from '../components/Toast';
import { blogsAPI, categoriesAPI, tagsAPI } from '../services/api';
import './AdminDashboard.css';

const AdminDashboard = () => {
  const { user, isAdmin } = useAuth();
  const { success, error } = useToast();
  const navigate = useNavigate();
  const [blogs, setBlogs] = useState([]);
  const [categories, setCategories] = useState([]);
  const [tags, setTags] = useState([]);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    author: user?.username || 'Admin',
    category: '',
    tags: [],
    featured: false,
    image_url: ''
  });

  useEffect(() => {
    if (!isAdmin()) {
      navigate('/');
      return;
    }
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [blogsRes, categoriesRes, tagsRes] = await Promise.all([
        blogsAPI.getAll({ page: 1, limit: 20 }),
        categoriesAPI.getAll(),
        tagsAPI.getAll()
      ]);
      setBlogs(blogsRes.data.blogs || []);
      setCategories(categoriesRes.data || []);
      setTags(tagsRes.data || []);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await blogsAPI.create(formData);
      success('Blog post created successfully!');
      setShowCreateForm(false);
      setFormData({
        title: '',
        content: '',
        author: user?.username || 'Admin',
        category: '',
        tags: [],
        featured: false,
        image_url: ''
      });
      fetchData();
    } catch (err) {
      error('Error creating blog post: ' + (err.response?.data?.detail || err.message));
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this post?')) return;
    
    try {
      await blogsAPI.delete(id);
      success('Blog post deleted successfully!');
      fetchData();
    } catch (err) {
      error('Error deleting blog post: ' + (err.response?.data?.detail || err.message));
    }
  };

  if (!isAdmin()) {
    return null;
  }

  return (
    <div className="admin-dashboard">
      <div className="container">
        <h1>Admin Dashboard</h1>
        <p>Welcome, {user?.username}! You are logged in as Admin.</p>

        <div className="admin-actions">
          <button onClick={() => setShowCreateForm(!showCreateForm)} className="btn btn-primary">
            {showCreateForm ? 'Cancel' : 'Create New Post'}
          </button>
        </div>

        {showCreateForm && (
          <form onSubmit={handleSubmit} className="create-post-form">
            <h2>Create New Blog Post</h2>
            
            <div className="form-group">
              <label>Title *</label>
              <input
                type="text"
                value={formData.title}
                onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                required
              />
            </div>

            <div className="form-group">
              <label>Content *</label>
              <textarea
                value={formData.content}
                onChange={(e) => setFormData({ ...formData, content: e.target.value })}
                rows="10"
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Author *</label>
                <input
                  type="text"
                  value={formData.author}
                  onChange={(e) => setFormData({ ...formData, author: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label>Category *</label>
                <select
                  value={formData.category}
                  onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                  required
                >
                  <option value="">Select Category</option>
                  {categories.map((cat) => (
                    <option key={cat._id} value={cat.name}>{cat.name}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="form-group">
              <label>Image URL</label>
              <input
                type="url"
                value={formData.image_url}
                onChange={(e) => setFormData({ ...formData, image_url: e.target.value })}
                placeholder="https://example.com/image.jpg"
              />
            </div>

            <div className="form-group">
              <label>Tags (comma-separated)</label>
              <input
                type="text"
                placeholder="Python, JavaScript, Tutorial"
                onChange={(e) => setFormData({ 
                  ...formData, 
                  tags: e.target.value.split(',').map(t => t.trim()).filter(t => t)
                })}
              />
            </div>

            <div className="form-group checkbox">
              <label>
                <input
                  type="checkbox"
                  checked={formData.featured}
                  onChange={(e) => setFormData({ ...formData, featured: e.target.checked })}
                />
                Featured Post
              </label>
            </div>

            <button type="submit" className="btn btn-primary">Create Post</button>
          </form>
        )}

        <div className="blog-list">
          <h2>All Blog Posts</h2>
          <div className="blog-table">
            {blogs.map((blog) => (
              <div key={blog._id} className="blog-row">
                <div className="blog-info">
                  <h3>{blog.title}</h3>
                  <p>{blog.category} | {blog.author}</p>
                </div>
                <div className="blog-actions">
                  <button onClick={() => navigate(`/blog/${blog._id}`)} className="btn btn-secondary">
                    View
                  </button>
                  <button onClick={() => handleDelete(blog._id)} className="btn btn-danger">
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
