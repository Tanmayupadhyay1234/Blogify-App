import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { categoriesAPI } from '../services/api';
import BlogCard from '../components/BlogCard';
import Sidebar from '../components/Sidebar';
import './CategoryPage.css';

const CategoryPage = () => {
  const { name } = useParams();
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);

  useEffect(() => {
    setPage(1);
    setBlogs([]);
    fetchBlogs(1);
  }, [name]);

  const fetchBlogs = async (currentPage) => {
    try {
      const response = await categoriesAPI.getPostsByCategory(name, {
        page: currentPage,
        limit: 12
      });
      if (currentPage === 1) {
        setBlogs(response.data.blogs);
      } else {
        setBlogs(prev => [...prev, ...response.data.blogs]);
      }
      setHasMore(currentPage < response.data.pages);
    } catch (error) {
      console.error('Error fetching blogs:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadMore = () => {
    const nextPage = page + 1;
    setPage(nextPage);
    fetchBlogs(nextPage);
  };

  return (
    <div className="category-page">
      <div className="container">
        <div className="category-header">
          <h1>{name}</h1>
          <p>Explore articles in {name}</p>
        </div>

        <div className="category-content">
          <div className="main-content">
            {loading && page === 1 ? (
              <div className="loading">Loading articles...</div>
            ) : blogs.length === 0 ? (
              <div className="no-results">No articles found in this category.</div>
            ) : (
              <>
                <div className="blog-grid">
                  {blogs.map(blog => (
                    <BlogCard key={blog._id} blog={blog} />
                  ))}
                </div>

                {hasMore && (
                  <div className="load-more">
                    <button onClick={loadMore} className="btn btn-outline">
                      Load More Articles
                    </button>
                  </div>
                )}
              </>
            )}
          </div>

          <Sidebar />
        </div>
      </div>
    </div>
  );
};

export default CategoryPage;
