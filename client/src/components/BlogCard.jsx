import React from 'react';
import { Link } from 'react-router-dom';
import LikeButton from './LikeButton';
import ReadingTime from './ReadingTime';
import './BlogCard.css';
import './BlogChatInterface.css';

const BlogCard = ({ blog }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  };

  return (
    <div className="blog-card">
      {blog.image_url && (
        <div className="blog-card-image">
          <img src={blog.image_url} alt={blog.title} />
          {blog.featured && <span className="featured-badge">Featured</span>}
        </div>
      )}
      <div className="blog-card-content">
        <div className="blog-card-meta">
          <Link to={`/category/${blog.category}`} className="category-tag">
            {blog.category}
          </Link>
          <span className="date">{formatDate(blog.created_at)}</span>
        </div>
        <Link to={`/blog/${blog._id}`}>
          <h3 className="blog-card-title">{blog.title}</h3>
        </Link>
        <p className="blog-card-excerpt">
          {blog.content.substring(0, 150)}...
        </p>
        <div className="blog-card-footer">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <span className="author">By {blog.author}</span>
            <ReadingTime content={blog.content} />
          </div>
          <div className="tags">
            {blog.tags && blog.tags.slice(0, 3).map((tag, index) => (
              <Link key={index} to={`/tag/${tag}`} className="tag">
                {tag}
              </Link>
            ))}
          </div>
        </div>
        <div style={{ marginTop: '15px' }}>
          <LikeButton blogId={blog._id} />
        </div>
      </div>
    </div>
  );
};

export default BlogCard;
