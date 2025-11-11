import React from 'react';
import { Link } from 'react-router-dom';
import { FiFacebook, FiTwitter, FiInstagram, FiLinkedin, FiMail } from 'react-icons/fi';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-col">
            <h3 className="footer-brand">Blogify</h3>
            <p className="footer-desc">
              Discover stories across every interest. Powered by AI for intelligent content discovery.
            </p>
            <div className="footer-social">
              <a href="https://facebook.com" className="social-icon" aria-label="Facebook"><FiFacebook /></a>
              <a href="https://twitter.com" className="social-icon" aria-label="Twitter"><FiTwitter /></a>
              <a href="https://instagram.com" className="social-icon" aria-label="Instagram"><FiInstagram /></a>
              <a href="https://linkedin.com" className="social-icon" aria-label="LinkedIn"><FiLinkedin /></a>
            </div>
          </div>

          <div className="footer-col">
            <h4 className="footer-title">Categories</h4>
            <ul className="footer-links">
              <li><Link to="/category/Technology">Technology</Link></li>
              <li><Link to="/category/Travel & Tourism">Travel</Link></li>
              <li><Link to="/category/Fashion & Style">Fashion</Link></li>
              <li><Link to="/category/Health & Wellness">Health</Link></li>
            </ul>
          </div>

          <div className="footer-col">
            <h4 className="footer-title">Quick Links</h4>
            <ul className="footer-links">
              <li><Link to="/">Home</Link></li>
              <li><Link to="/">Trending</Link></li>
              <li><Link to="/">About</Link></li>
              <li><Link to="/">Contact</Link></li>
            </ul>
          </div>

          <div className="footer-col">
            <h4 className="footer-title">Newsletter</h4>
            <p className="footer-newsletter-text">
              Get the latest articles delivered to your inbox.
            </p>
            <div className="newsletter-form">
              <input type="email" placeholder="Your email" className="newsletter-input" />
              <button className="newsletter-btn">
                <FiMail />
              </button>
            </div>
          </div>
        </div>

        <div className="footer-bottom">
          <p>&copy; 2025 Blogify. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
