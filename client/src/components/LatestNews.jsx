import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './LatestNews.css';

const LatestNews = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [expandedId, setExpandedId] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL || 'http://localhost:5010'}/api/latest-news?limit=15`);
        setNews(response.data);
      } catch (error) {
        console.error('Error fetching news:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchNews();
  }, []);

  if (loading) return <div className="latest-news-loading">Loading news...</div>;
  if (!news.length) return null;

  return (
    <div className="latest-news-section">
      <div className="latest-news-header">
        <h2>🔥 Latest News</h2>
        <span className="news-badge">Live</span>
      </div>
      <div className="news-ticker">
        {news.map((item, index) => (
          <div 
            key={item._id || index} 
            className={`news-item ${expandedId === item._id ? 'expanded' : ''}`}
            onClick={() => setExpandedId(expandedId === item._id ? null : item._id)}
          >
            <span className="news-category">{item.category}</span>
            <h4>{item.headline}</h4>
            <p className={expandedId === item._id ? 'expanded' : ''}>{item.summary}</p>
            <span className="news-time">{new Date(item.created_at).toLocaleString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default LatestNews;
