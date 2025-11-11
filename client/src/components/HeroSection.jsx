import React from 'react';
import { Link } from 'react-router-dom';

const HeroSection = ({ featuredPost }) => {
  if (!featuredPost) return null;

  return (
    <div className="relative h-[500px] mb-12 rounded-xl overflow-hidden shadow-2xl">
      <div 
        className="absolute inset-0 bg-cover bg-center transform hover:scale-105 transition-transform duration-700"
        style={{ 
          backgroundImage: `url(${featuredPost.image_url || 'https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=1200'})` 
        }}
      />
      <div className="absolute inset-0 bg-gradient-to-t from-black via-black/50 to-transparent" />
      
      <div className="absolute bottom-0 left-0 right-0 p-12 text-white">
        <span className="inline-block bg-blue-600 px-4 py-2 rounded-lg text-sm font-semibold mb-4 hover:bg-blue-700 transition">
          {featuredPost.category}
        </span>
        
        <h1 className="text-5xl font-bold mb-4 max-w-3xl leading-tight">
          {featuredPost.title}
        </h1>
        
        <p className="text-xl mb-6 max-w-2xl text-gray-200">
          {featuredPost.content.substring(0, 200)}...
        </p>
        
        <div className="flex items-center space-x-6">
          <Link 
            to={`/blog/${featuredPost._id}`}
            className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-lg font-semibold transition transform hover:scale-105"
          >
            Read Article →
          </Link>
          
          <div className="flex items-center space-x-4 text-sm">
            <span className="font-medium">{featuredPost.author}</span>
            <span>•</span>
            <span>{new Date(featuredPost.created_at).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
