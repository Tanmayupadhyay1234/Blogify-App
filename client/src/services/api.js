import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5010';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const userStr = localStorage.getItem('user');
  if (userStr) {
    const user = JSON.parse(userStr);
    if (user.access_token) {
      config.headers['Authorization'] = `Bearer ${user.access_token}`;
    }
  }
  return config;
});

export const authAPI = {
  login: (username, role) => api.post('/api/auth/login', { username, role }),
};

export const blogsAPI = {
  getAll: (params) => api.get('/api/blogs', { params }),
  getById: (id) => api.get(`/api/blogs/${id}`),
  getFeatured: () => api.get('/api/blogs/featured'),
  getTrending: (limit = 10) => api.get('/api/blogs/trending', { params: { limit } }),
  getRelated: (id) => api.get(`/api/blogs/${id}/related`),
  create: (data) => api.post('/api/blogs', data),
  update: (id, data) => api.put(`/api/blogs/${id}`, data),
  delete: (id) => api.delete(`/api/blogs/${id}`),
};

export const categoriesAPI = {
  getAll: () => api.get('/api/categories'),
  getPostsByCategory: (name, params) => api.get(`/api/categories/${name}/posts`, { params }),
  create: (data) => api.post('/api/categories', data),
};

export const tagsAPI = {
  getAll: () => api.get('/api/tags'),
  getPostsByTag: (name, params) => api.get(`/api/tags/${name}/posts`, { params }),
  create: (data) => api.post('/api/tags', data),
};

export const searchAPI = {
  search: (query) => api.get('/api/search', { params: { q: query } }),
};

export const aiAPI = {
  summarize: (blogId) => api.post('/api/ai/summarize', { blog_id: blogId }),
  chat: (query, blogId) => api.post('/api/ai/chat', { query, blog_id: blogId }),
};

export default api;
