import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useToast } from '../components/Toast';
import { authAPI } from '../services/api';
import './Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [role, setRole] = useState('user');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const { success, error } = useToast();
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await authAPI.login(username || 'Guest', role);
      login(response.data);
      success(`Welcome ${username || 'Guest'}! Logged in as ${role}`);
      navigate('/');
    } catch (err) {
      error('Login failed. Please try again.');
      console.error('Login error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <div className="login-header">
          <h1>Welcome to TechInsight</h1>
          <p>Sign in to access your personalized magazine experience</p>
        </div>

        <form className="login-form" onSubmit={handleLogin}>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              placeholder="Enter your username (optional)"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              placeholder="Enter your password (not required)"
              className="form-input"
            />
            <small className="form-hint">
              No password required - just click Sign In!
            </small>
          </div>

          <div className="role-toggle">
            <label className="toggle-label">Sign in as:</label>
            <div className="toggle-buttons">
              <button
                type="button"
                className={`toggle-btn ${role === 'user' ? 'active' : ''}`}
                onClick={() => setRole('user')}
              >
                User
              </button>
              <button
                type="button"
                className={`toggle-btn ${role === 'admin' ? 'active' : ''}`}
                onClick={() => setRole('admin')}
              >
                Admin
              </button>
            </div>
          </div>

          <button type="submit" className="btn btn-primary btn-login" disabled={loading}>
            {loading ? 'Signing In...' : 'Sign In'}
          </button>

          <p className="login-note">
            <strong>Instant Login:</strong> Click "Sign In" to access the platform instantly.
            Username is optional, and no password is required!
          </p>
        </form>
      </div>
    </div>
  );
};

export default Login;
