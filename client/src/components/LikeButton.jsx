import React, { useState, useEffect } from 'react';
import { FiHeart } from 'react-icons/fi';

const LikeButton = ({ blogId }) => {
  const [liked, setLiked] = useState(false);
  const [likeCount, setLikeCount] = useState(0);

  useEffect(() => {
    // Check if user has liked this post
    const likedPosts = JSON.parse(localStorage.getItem('likedPosts') || '{}');
    setLiked(!!likedPosts[blogId]);
    
    // Get like count from localStorage (in production, fetch from API)
    const counts = JSON.parse(localStorage.getItem('likeCounts') || '{}');
    setLikeCount(counts[blogId] || 0);
  }, [blogId]);

  const handleLike = () => {
    const likedPosts = JSON.parse(localStorage.getItem('likedPosts') || '{}');
    const counts = JSON.parse(localStorage.getItem('likeCounts') || '{}');

    if (liked) {
      // Unlike
      delete likedPosts[blogId];
      counts[blogId] = Math.max(0, (counts[blogId] || 0) - 1);
      setLiked(false);
      setLikeCount(counts[blogId]);
    } else {
      // Like
      likedPosts[blogId] = true;
      counts[blogId] = (counts[blogId] || 0) + 1;
      setLiked(true);
      setLikeCount(counts[blogId]);
    }

    localStorage.setItem('likedPosts', JSON.stringify(likedPosts));
    localStorage.setItem('likeCounts', JSON.stringify(counts));
  };

  return (
    <button
      onClick={handleLike}
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: '6px',
        padding: '8px 16px',
        borderRadius: '8px',
        fontSize: '14px',
        fontWeight: '600',
        border: '1.5px solid',
        transition: 'all 0.3s ease',
        cursor: 'pointer',
        background: liked ? '#ef4444' : 'transparent',
        color: liked ? 'white' : 'var(--text-primary)',
        borderColor: liked ? '#ef4444' : 'var(--border-color)'
      }}
      onMouseEnter={(e) => {
        if (!liked) {
          e.currentTarget.style.borderColor = '#ef4444';
          e.currentTarget.style.color = '#ef4444';
        }
      }}
      onMouseLeave={(e) => {
        if (!liked) {
          e.currentTarget.style.borderColor = 'var(--border-color)';
          e.currentTarget.style.color = 'var(--text-primary)';
        }
      }}
    >
      <FiHeart 
        style={{
          width: '16px',
          height: '16px',
          fill: liked ? 'currentColor' : 'none'
        }}
      />
      <span>{likeCount > 0 ? likeCount : 'Like'}</span>
    </button>
  );
};

export default LikeButton;
