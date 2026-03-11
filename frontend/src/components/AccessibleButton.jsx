import React from 'react';

export const AccessibleButton = ({ label, onClick, children, variant = 'primary' }) => (
  <button
    aria-label={label}
    onClick={onClick}
    className={`btn btn-${variant} focus-visible:ring-2 focus-visible:ring-blue-600`}
  >
    {children}
  </button>
);
