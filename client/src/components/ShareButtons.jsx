import React, { useState } from 'react';
import { FiShare2, FiTwitter, FiLinkedin, FiCopy, FiCheck } from 'react-icons/fi';

const ShareButtons = ({ title, url }) => {
  const [copied, setCopied] = useState(false);
  const [showMenu, setShowMenu] = useState(false);

  const shareUrl = url || window.location.href;
  const shareTitle = encodeURIComponent(title);

  const handleCopy = () => {
    navigator.clipboard.writeText(shareUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const shareLinks = {
    twitter: `https://twitter.com/intent/tweet?text=${shareTitle}&url=${shareUrl}`,
    linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${shareUrl}`,
  };

  return (
    <div className="relative">
      <button
        onClick={() => setShowMenu(!showMenu)}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          padding: '8px 16px',
          borderRadius: '8px',
          fontSize: '14px',
          fontWeight: '600',
          border: '1.5px solid var(--border-color)',
          background: 'transparent',
          color: 'var(--text-primary)',
          cursor: 'pointer',
          transition: 'all 0.3s ease'
        }}
        onMouseEnter={(e) => {
          e.currentTarget.style.borderColor = '#3b82f6';
          e.currentTarget.style.color = '#3b82f6';
        }}
        onMouseLeave={(e) => {
          e.currentTarget.style.borderColor = 'var(--border-color)';
          e.currentTarget.style.color = 'var(--text-primary)';
        }}
      >
        <FiShare2 style={{ width: '16px', height: '16px' }} />
        <span>Share</span>
      </button>

      {showMenu && (
        <>
          <div 
            className="fixed inset-0 z-40" 
            onClick={() => setShowMenu(false)}
          />
          <div style={{
            position: 'absolute',
            right: 0,
            marginTop: '8px',
            width: '220px',
            background: 'var(--bg-primary)',
            borderRadius: '12px',
            boxShadow: '0 8px 24px var(--card-shadow)',
            border: '1px solid var(--border-color)',
            padding: '8px 0',
            zIndex: 50,
            overflow: 'hidden'
          }}>
            <a
              href={shareLinks.twitter}
              target="_blank"
              rel="noopener noreferrer"
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                padding: '12px 16px',
                color: 'var(--text-primary)',
                transition: 'background 0.2s ease',
                textDecoration: 'none'
              }}
              onMouseEnter={(e) => e.currentTarget.style.background = 'var(--bg-tertiary)'}
              onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
            >
              <FiTwitter style={{ width: '18px', height: '18px', color: '#1DA1F2' }} />
              <span style={{ fontSize: '14px', fontWeight: '500' }}>Twitter</span>
            </a>

            <a
              href={shareLinks.linkedin}
              target="_blank"
              rel="noopener noreferrer"
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                padding: '12px 16px',
                color: 'var(--text-primary)',
                transition: 'background 0.2s ease',
                textDecoration: 'none'
              }}
              onMouseEnter={(e) => e.currentTarget.style.background = 'var(--bg-tertiary)'}
              onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
            >
              <FiLinkedin style={{ width: '18px', height: '18px', color: '#0A66C2' }} />
              <span style={{ fontSize: '14px', fontWeight: '500' }}>LinkedIn</span>
            </a>

            <div style={{ borderTop: '1px solid var(--border-color)', margin: '4px 0' }}></div>

            <button
              onClick={handleCopy}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                padding: '12px 16px',
                width: '100%',
                textAlign: 'left',
                background: 'transparent',
                border: 'none',
                color: 'var(--text-primary)',
                cursor: 'pointer',
                transition: 'background 0.2s ease'
              }}
              onMouseEnter={(e) => e.currentTarget.style.background = 'var(--bg-tertiary)'}
              onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
            >
              {copied ? (
                <>
                  <FiCheck style={{ width: '18px', height: '18px', color: '#10b981' }} />
                  <span style={{ fontSize: '14px', fontWeight: '500', color: '#10b981' }}>Copied!</span>
                </>
              ) : (
                <>
                  <FiCopy style={{ width: '18px', height: '18px' }} />
                  <span style={{ fontSize: '14px', fontWeight: '500' }}>Copy Link</span>
                </>
              )}
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default ShareButtons;
