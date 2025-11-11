import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { blogsAPI } from '../services/api';
import './FeaturedPosts.css';

const FeaturedPosts = () => {
  const [featuredPosts, setFeaturedPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFeaturedPosts = async () => {
      try {
        const response = await blogsAPI.getFeatured();
        setFeaturedPosts(response.data);
      } catch (error) {
        console.error('Error fetching featured posts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchFeaturedPosts();
  }, []);

  if (loading) return <div className="loading">Loading featured posts...</div>;

  if (featuredPosts.length === 0) return null;

  const mainPost = featuredPosts[0];
  const sidePosts = featuredPosts.slice(1, 3);

  return (
    <section className="featured-posts">
      <h2 className="section-title">Featured Stories</h2>
      <div className="featured-grid">
        <Link to={`/blog/${mainPost._id}`} className="featured-main">
          <div className="featured-image">
            <img src={mainPost.image_url} alt={mainPost.title} />
          </div>
          <div className="featured-content">
            <span className="featured-category">{mainPost.category}</span>
            <h3 className="featured-title">{mainPost.title}</h3>
            <p className="featured-excerpt">
              {mainPost.content.substring(0, 200)}...
            </p>
            <div className="featured-meta">
              <span>By {mainPost.author}</span>
              <span>•</span>
              <span>{new Date(mainPost.created_at).toLocaleDateString()}</span>
            </div>
          </div>
        </Link>

        <div className="featured-side">
          {sidePosts.map((post) => (
            <Link key={post._id} to={`/blog/${post._id}`} className="featured-side-item">
              <div className="featured-side-image">
                <img src={post.image_url} alt={post.title} />
              </div>
              <div className="featured-side-content">
                <span className="featured-category">{post.category}</span>
                <h4 className="featured-side-title">{post.title}</h4>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeaturedPosts;
