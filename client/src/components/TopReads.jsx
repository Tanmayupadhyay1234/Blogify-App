import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { blogsAPI } from '../services/api';

const TopReads = () => {
  const [topPosts, setTopPosts] = useState([]);

  useEffect(() => {
    blogsAPI.getFeatured().then(res => {
      setTopPosts(res.data.slice(0, 4) || []);
    });
  }, []);

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mt-6">
      <h3 className="text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600">Top Reads</h3>
      <div className="space-y-4">
        {topPosts.map((post) => (
          <Link 
            key={post._id} 
            to={`/blog/${post._id}`}
            className="block hover:bg-gray-50 p-2 rounded transition"
          >
            {post.image_url && (
              <img 
                src={post.image_url} 
                alt={post.title}
                className="w-full h-32 object-cover rounded mb-2"
              />
            )}
            <h4 className="font-semibold text-sm hover:text-blue-600 line-clamp-2 mb-1">
              {post.title}
            </h4>
            <div className="flex items-center gap-2 text-xs text-gray-500">
              <span className="bg-blue-100 text-blue-600 px-2 py-1 rounded">{post.category}</span>
              <span>{new Date(post.created_at).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}</span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default TopReads;
