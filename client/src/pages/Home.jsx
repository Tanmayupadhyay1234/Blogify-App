import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { blogsAPI } from '../services/api';
import { FiClock, FiEye, FiHeart, FiTrendingUp } from 'react-icons/fi';
import LatestNews from '../components/LatestNews';
import LoadingSpinner from '../components/LoadingSpinner';
import './Home.css';

const Home = () => {
  const [featuredPosts, setFeaturedPosts] = useState([]);
  const [currentFeaturedIndex, setCurrentFeaturedIndex] = useState(0);
  const [trending, setTrending] = useState([]);
  const [allTrending, setAllTrending] = useState([]);
  const [sortBy, setSortBy] = useState('views');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [featuredRes, trendingRes] = await Promise.all([
          blogsAPI.getFeatured(),
          blogsAPI.getTrending(20)
        ]);
        setFeaturedPosts(featuredRes.data || []);
        setAllTrending(trendingRes.data);
        setTrending(trendingRes.data.slice(0, 8));
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    if (featuredPosts.length > 0) {
      const interval = setInterval(() => {
        setCurrentFeaturedIndex((prev) => (prev + 1) % featuredPosts.length);
      }, 5000);
      return () => clearInterval(interval);
    }
  }, [featuredPosts]);

  const handleSort = (type) => {
    setSortBy(type);
    let sorted = [...allTrending];
    if (type === 'views') {
      sorted.sort((a, b) => (b.views || 0) - (a.views || 0));
    } else if (type === 'likes') {
      sorted.sort((a, b) => (b.likes || 0) - (a.likes || 0));
    } else if (type === 'recent') {
      sorted.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    }
    setTrending(sorted.slice(0, 8));
  };

  const calculateReadTime = (content) => {
    const words = content.split(' ').length;
    return Math.ceil(words / 200);
  };

  if (loading) return <LoadingSpinner text="Loading amazing content..." />;

  const featuredPost = featuredPosts[currentFeaturedIndex];

  return (
    <div className="home-modern">
      {/* Hero Section */}
      {featuredPost && (
        <section className="hero-section">
          <div className="hero-overlay" />
          <img src={featuredPost.image_url} alt={featuredPost.title} className="hero-bg" />
          <div className="hero-content">
            <span className="hero-category">{featuredPost.category}</span>
            <h1 className="hero-title">{featuredPost.title}</h1>
            <p className="hero-description">
              {featuredPost.content.substring(0, 150)}...
            </p>
            <div className="hero-meta">
              <span><FiClock /> {calculateReadTime(featuredPost.content)} min read</span>
              <span><FiEye /> {featuredPost.views || 0} views</span>
            </div>
            <Link to={`/blog/${featuredPost._id}`} className="hero-btn">
              Read Article →
            </Link>
          </div>
          <div className="hero-indicators">
            {featuredPosts.map((_, index) => (
              <button
                key={index}
                className={`indicator ${index === currentFeaturedIndex ? 'active' : ''}`}
                onClick={() => setCurrentFeaturedIndex(index)}
              />
            ))}
          </div>
        </section>
      )}

      {/* Trending Section */}
      <section className="trending-section-home">
        <div className="container">
          <div className="section-header">
            <h2 className="section-heading">
              <FiTrendingUp /> Trending Now
            </h2>
            <div className="section-actions">
              <button 
                className={`sort-btn ${sortBy === 'views' ? 'active' : ''}`}
                onClick={() => handleSort('views')}
              >
                Most Viewed
              </button>
              <button 
                className={`sort-btn ${sortBy === 'likes' ? 'active' : ''}`}
                onClick={() => handleSort('likes')}
              >
                Most Liked
              </button>
              <button 
                className={`sort-btn ${sortBy === 'recent' ? 'active' : ''}`}
                onClick={() => handleSort('recent')}
              >
                Recent
              </button>
              <Link to="/categories" className="view-all-btn">View All</Link>
            </div>
          </div>
          <div className="trending-grid">
            {trending.map((post) => (
              <Link key={post._id} to={`/blog/${post._id}`} className="trending-card">
                <img src={post.image_url} alt={post.title} className="trending-img" />
                <div className="trending-content">
                  <span className="trending-category">{post.category}</span>
                  <h3 className="trending-title">{post.title}</h3>
                  <div className="trending-stats">
                    <span><FiEye /> {post.views || 0}</span>
                    <span><FiHeart /> {post.likes || 0}</span>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Latest News Section */}
      <section className="news-section">
        <div className="container">
          <LatestNews />
        </div>
      </section>
    </div>
  );
};

export default Home;
