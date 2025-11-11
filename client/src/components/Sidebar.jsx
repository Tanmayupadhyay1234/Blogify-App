import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { categoriesAPI, tagsAPI } from '../services/api';
import './Sidebar.css';

const Sidebar = () => {
  const [categories, setCategories] = useState([]);
  const [tags, setTags] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [categoriesRes, tagsRes] = await Promise.all([
          categoriesAPI.getAll(),
          tagsAPI.getAll()
        ]);
        setCategories(categoriesRes.data);
        setTags(tagsRes.data);
      } catch (error) {
        console.error('Error fetching sidebar data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <aside className="sidebar">
      <div className="sidebar-section">
        <h3 className="sidebar-title">Categories</h3>
        <ul className="sidebar-list">
          {categories.map((category) => (
            <li key={category._id}>
              <Link to={`/category/${category.name}`} className="sidebar-link">
                {category.name}
              </Link>
            </li>
          ))}
        </ul>
      </div>

      <div className="sidebar-section">
        <h3 className="sidebar-title">Popular Tags</h3>
        <div className="tag-cloud">
          {tags.slice(0, 15).map((tag) => (
            <Link
              key={tag._id}
              to={`/tag/${tag.name}`}
              className="tag-cloud-item"
            >
              {tag.name}
            </Link>
          ))}
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
