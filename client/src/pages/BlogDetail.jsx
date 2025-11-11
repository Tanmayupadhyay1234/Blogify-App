import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { blogsAPI } from '../services/api';
import ShareButtons from '../components/ShareButtons';
import LikeButton from '../components/LikeButton';
import ReadingTime from '../components/ReadingTime';
import BlogChatInterface from '../components/BlogChatInterface';
import { FiEye, FiCalendar, FiMessageCircle, FiX } from 'react-icons/fi';
import './BlogDetail.css';

const BlogDetail = () => {
  const { id } = useParams();
  const [blog, setBlog] = useState(null);
  const [relatedPosts, setRelatedPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [chatOpen, setChatOpen] = useState(false);

  useEffect(() => {
    setLoading(true);
    window.scrollTo(0, 0);
    
    const fetchBlog = async () => {
      try {
        const [blogRes, relatedRes] = await Promise.all([
          blogsAPI.getById(id),
          blogsAPI.getRelated(id)
        ]);
        setBlog(blogRes.data);
        setRelatedPosts(relatedRes.data);
      } catch (error) {
        console.error('Error fetching blog:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchBlog();
  }, [id]);

  const toggleChat = () => {
    setChatOpen(!chatOpen);
  };

  if (loading) return <div className="loading">Loading article...</div>;
  if (!blog) return <div className="error">Blog post not found</div>;

  return (
    <div className="blog-detail">
      {/* Hero Image Section */}
      {blog.image_url && (
        <div className="blog-hero">
          <img src={blog.image_url} alt={blog.title} className="blog-hero-img" />
          <div className="blog-hero-overlay" />
          <div className="blog-hero-content">
            <Link to={`/category/${blog.category}`} className="hero-category-badge">
              {blog.category}
            </Link>
            <h1 className="hero-title">{blog.title}</h1>
          </div>
        </div>
      )}

      <div className="container">
        <article className="blog-article">
          <header className="blog-header">
            <div className="blog-author-section">
              <div className="author-avatar">
                {blog.author.charAt(0).toUpperCase()}
              </div>
              <div className="author-info">
                <h4 className="author-name">{blog.author}</h4>
                <div className="blog-meta">
                  <span className="meta-item">
                    <FiCalendar />
                    {new Date(blog.created_at).toLocaleDateString('en-US', {
                      month: 'long',
                      day: 'numeric',
                      year: 'numeric'
                    })}
                  </span>
                  <span className="meta-dot">•</span>
                  <ReadingTime content={blog.content} />
                </div>
              </div>
              <div className="blog-actions">
                <LikeButton blogId={blog._id} />
                <ShareButtons title={blog.title} />
                <span className="views-count">
                  <FiEye /> {blog.views || 0}
                </span>
              </div>
            </div>
          </header>

          {blog.image_url && (
            <div className="blog-image">
              <img src={blog.image_url} alt={blog.title} />
            </div>
          )}

          <div className="blog-content">
            {blog.content.split('\n\n').filter(p => p.trim()).map((paragraph, index) => (
              <p key={index}>{paragraph}</p>
            ))}
          </div>

          <div className="blog-tags">
            {blog.tags && blog.tags.map((tag, index) => (
              <Link key={index} to={`/tag/${tag}`} className="tag">
                #{tag}
              </Link>
            ))}
          </div>
        </article>

        {relatedPosts.length > 0 && (
          <section className="related-posts">
            <h2>Related Articles</h2>
            <div className="related-grid">
              {relatedPosts.map(post => (
                <Link key={post._id} to={`/blog/${post._id}`} className="related-card">
                  {post.image_url && (
                    <img src={post.image_url} alt={post.title} />
                  )}
                  <div className="related-content">
                    <span className="related-category">{post.category}</span>
                    <h4>{post.title}</h4>
                  </div>
                </Link>
              ))}
            </div>
          </section>
        )}
      </div>

      {/* Floating Chat Widget */}
      <div className="floating-chat-widget">
        {!chatOpen && (
          <button className="chat-toggle-btn" onClick={toggleChat} title="Ask about this article">
            <FiMessageCircle />
          </button>
        )}

        {chatOpen && (
          <div className="chat-window">
            <div className="chat-window-header">
              <div className="chat-window-header-content">
                <h3>
                  <FiMessageCircle /> Ask About Article
                </h3>
                <p>Get instant answers about this content</p>
              </div>
              <button className="chat-close-btn" onClick={toggleChat}>
                <FiX />
              </button>
            </div>
            <div className="chat-window-body">
              <BlogChatInterface blogId={blog._id} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default BlogDetail;
