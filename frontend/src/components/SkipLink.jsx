import React from 'react';

export const SkipLink = ({ targetId = 'main-content', children = 'Skip to main content' }) => (
  <a
    href={`#${targetId}`}
    className="skip-link"
    onClick={(e) => {
      e.preventDefault();
      document.getElementById(targetId)?.focus();
    }}
  >
    {children}
  </a>
);
