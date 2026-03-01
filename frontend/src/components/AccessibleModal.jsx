import React, { useRef, useEffect } from 'react';
import { useFocusTrap } from '../hooks/useFocusTrap';

export const AccessibleModal = ({ isOpen, onClose, title, children }) => {
  const modalRef = useRef(null);
  useFocusTrap(modalRef, isOpen);

  useEffect(() => {
    const handleEscape = (e) => e.key === 'Escape' && onClose();
    if (isOpen) {
      document.addEventListener('keydown', handleEscape);
      document.body.style.overflow = 'hidden';
    }
    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = 'auto';
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div role="overlay" className="fixed inset-0 bg-black/50" onClick={onClose}>
      <div
        ref={modalRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        className="modal-content"
        onClick={e => e.stopPropagation()}
      >
        <h2 id="modal-title">{title}</h2>
        <button aria-label="Close modal" onClick={onClose}>×</button>
        {children}
      </div>
    </div>
  );
};
