import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { tagsAPI } from '../services/api';
import BlogCard from '../components/BlogCard';
import Sidebar from '../components/Sidebar';
import './TagPage.css';

const TagPage = () => {
  const { name } = useParams();
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBlogs = async () => {
      try {
        const response = await tagsAPI.getPostsByTag(name, { page: 1, limit: 20 });
        setBlogs(response.data.blogs);
      } catch (error) {
        console.error('Error fetching blogs:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchBlogs();
  }, [name]);

  return (
    <div className="tag-page">
      <div className="container">
        <div className="tag-header">
          <h1>#{name}</h1>
          <p>Articles tagged with {name}</p>
        </div>

        <div className="tag-content">
          <div className="main-content">
            {loading ? (
              <div className="loading">Loading articles...</div>
            ) : blogs.length === 0 ? (
              <div className="no-results">No articles found with this tag.</div>
            ) : (
              <div className="blog-grid">
                {blogs.map(blog => (
                  <BlogCard key={blog._id} blog={blog} />
                ))}
              </div>
            )}
          </div>

          <Sidebar />
        </div>
      </div>
    </div>
  );
};

export default TagPage;
