import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { searchAPI } from '../services/api';
import { FiSun, FiMoon, FiSearch, FiMenu, FiUser, FiLogOut } from 'react-icons/fi';
import './Navbar.css';

const Navbar = () => {
  const { user, logout } = useAuth();
  const { darkMode, toggleDarkMode } = useTheme();
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  const [categoriesOpen, setCategoriesOpen] = useState(false);
  const [userMenuOpen, setUserMenuOpen] = useState(false);

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery)}`);
      setSearchQuery('');
      setShowSuggestions(false);
    }
  };

  const handleSearchChange = async (e) => {
    const query = e.target.value;
    setSearchQuery(query);
    
    if (query.length > 2) {
      try {
        const response = await searchAPI.search(query);
        setSuggestions(response.data.slice(0, 5));
        setShowSuggestions(true);
      } catch (error) {
        console.error('Error fetching suggestions:', error);
      }
    } else {
      setShowSuggestions(false);
    }
  };

  const handleSuggestionClick = () => {
    setShowSuggestions(false);
    setSearchQuery('');
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-left">
          <Link to="/" className="navbar-brand">
            <h1>Blogify</h1>
          </Link>

          <div className="navbar-menu">
            <Link to="/" className="nav-link">Home</Link>
            <Link to="/categories" className="nav-link">Categories</Link>
            <Link to="/" className="nav-link">Trending</Link>
          </div>
        </div>

        <div className="navbar-actions">
          {searchOpen ? (
            <form onSubmit={handleSearch} className="search-form-expanded">
              <input
                type="text"
                placeholder="Search articles..."
                value={searchQuery}
                onChange={handleSearchChange}
                onBlur={() => setTimeout(() => { setSearchOpen(false); setShowSuggestions(false); }, 200)}
                className="search-input"
                autoFocus
              />
              {showSuggestions && suggestions.length > 0 && (
                <div className="suggestions-dropdown">
                  {suggestions.map(blog => (
                    <Link 
                      key={blog._id} 
                      to={`/blog/${blog._id}`}
                      className="suggestion-item"
                      onClick={handleSuggestionClick}
                    >
                      <span className="suggestion-title">{blog.title}</span>
                      <span className="suggestion-category">{blog.category}</span>
                    </Link>
                  ))}
                </div>
              )}
            </form>
          ) : (
            <button onClick={() => setSearchOpen(true)} className="icon-btn">
              <FiSearch size={20} />
            </button>
          )}

          <button onClick={toggleDarkMode} className="icon-btn" title={darkMode ? 'Light Mode' : 'Dark Mode'}>
            {darkMode ? <FiSun size={20} /> : <FiMoon size={20} />}
          </button>

          {user ? (
            <div className="nav-dropdown">
              <button 
                className="user-btn"
                onClick={() => setUserMenuOpen(!userMenuOpen)}
                onBlur={() => setTimeout(() => setUserMenuOpen(false), 200)}
              >
                <FiUser size={16} />
                <span className="user-name">{user.username}</span>
                {user.role === 'admin' && <span className="badge">Admin</span>}
              </button>
              {userMenuOpen && (
                <div className="dropdown-menu dropdown-menu-right">
                  {user.role === 'admin' && (
                    <Link to="/admin" className="dropdown-item">Dashboard</Link>
                  )}
                  <button onClick={logout} className="dropdown-item">
                    <FiLogOut size={16} /> Logout
                  </button>
                </div>
              )}
            </div>
          ) : (
            <Link to="/login" className="btn btn-primary">Login</Link>
          )}

          <button className="icon-btn mobile-menu">
            <FiMenu size={20} />
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
