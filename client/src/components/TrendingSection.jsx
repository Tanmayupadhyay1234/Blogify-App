import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { blogsAPI } from '../services/api';
import { FiTrendingUp, FiEye } from 'react-icons/fi';
import './TrendingSection.css';

const TrendingSection = () => {
  const [trending, setTrending] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTrending = async () => {
      try {
        const response = await blogsAPI.getTrending(5);
        setTrending(response.data);
      } catch (error) {
        console.error('Error fetching trending posts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchTrending();
  }, []);

  if (loading) return null;
  if (trending.length === 0) return null;

  return (
    <section className="trending-section">
      <div className="trending-header">
        <FiTrendingUp className="trending-icon" />
        <h2>Trending Now</h2>
      </div>
      <div className="trending-list">
        {trending.map((post, index) => (
          <Link key={post._id} to={`/blog/${post._id}`} className="trending-item">
            <span className="trending-rank">#{index + 1}</span>
            <div className="trending-content">
              <h4>{post.title}</h4>
              <div className="trending-meta">
                <span className="trending-category">{post.category}</span>
                <span className="trending-views">
                  <FiEye size={14} />
                  {post.views || 0}
                </span>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </section>
  );
};

export default TrendingSection;
