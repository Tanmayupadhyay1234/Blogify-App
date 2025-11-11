import React from 'react';
import { FiClock } from 'react-icons/fi';

const ReadingTime = ({ content }) => {
  const calculateReadingTime = (text) => {
    const wordsPerMinute = 200;
    const words = text.trim().split(/\s+/).length;
    const minutes = Math.ceil(words / wordsPerMinute);
    return minutes;
  };

  const minutes = calculateReadingTime(content);

  return (
    <span className="meta-item">
      <FiClock />
      {minutes} min read
    </span>
  );
};

export default ReadingTime;
