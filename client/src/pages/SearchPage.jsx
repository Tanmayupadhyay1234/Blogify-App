import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { searchAPI } from '../services/api';
import BlogCard from '../components/BlogCard';
import './SearchPage.css';

const SearchPage = () => {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('q');
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (query) {
      searchBlogs();
    }
  }, [query]);

  const searchBlogs = async () => {
    setLoading(true);
    try {
      const response = await searchAPI.search(query);
      setBlogs(response.data);
    } catch (error) {
      console.error('Error searching blogs:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="search-page">
      <div className="container">
        <div className="search-header">
          <h1>Search Results</h1>
          <p>Showing results for: <strong>{query}</strong></p>
        </div>

        {loading ? (
          <div className="loading">Searching...</div>
        ) : blogs.length === 0 ? (
          <div className="no-results">
            <h2>No results found</h2>
            <p>Try searching with different keywords</p>
          </div>
        ) : (
          <div className="results">
            <p className="results-count">{blogs.length} article{blogs.length !== 1 ? 's' : ''} found</p>
            <div className="blog-grid">
              {blogs.map(blog => (
                <BlogCard key={blog._id} blog={blog} />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SearchPage;
