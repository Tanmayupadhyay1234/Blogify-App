import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { categoriesAPI, blogsAPI } from '../services/api';
import BlogCard from '../components/BlogCard';
import LoadingSpinner from '../components/LoadingSpinner';
import './CategoriesPage.css';

const CategoriesPage = () => {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchCategories();
    fetchBlogs('all');
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await categoriesAPI.getAll();
      setCategories(response.data);
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  };

  const fetchBlogs = async (category) => {
    setLoading(true);
    try {
      if (category === 'all') {
        const response = await blogsAPI.getAll({ page: 1, limit: 50 });
        setBlogs(response.data.blogs);
      } else {
        const response = await categoriesAPI.getPostsByCategory(category, { page: 1, limit: 50 });
        setBlogs(response.data.blogs);
      }
    } catch (error) {
      console.error('Error fetching blogs:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
    fetchBlogs(category);
  };

  return (
    <div className="categories-page">
      <div className="container">
        <div className="categories-header">
          <h1>Explore Categories</h1>
          <p>Discover content across all topics</p>
        </div>

        <div className="categories-nav">
          <button
            className={`category-btn ${selectedCategory === 'all' ? 'active' : ''}`}
            onClick={() => handleCategoryClick('all')}
          >
            All
          </button>
          {categories.map((cat) => (
            <button
              key={cat._id}
              className={`category-btn ${selectedCategory === cat.name ? 'active' : ''}`}
              onClick={() => handleCategoryClick(cat.name)}
            >
              {cat.name}
            </button>
          ))}
        </div>

        {loading ? (
          <LoadingSpinner text="Loading articles..." />
        ) : blogs.length === 0 ? (
          <div className="no-results">No articles found in this category.</div>
        ) : (
          <div className="blog-grid">
            {blogs.map(blog => (
              <BlogCard key={blog._id} blog={blog} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default CategoriesPage;
