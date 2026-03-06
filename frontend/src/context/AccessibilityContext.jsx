import React, { createContext, useContext, useState, useEffect } from 'react';

const AccessibilityContext = createContext();

export const AccessibilityProvider = ({ children }) => {
  const [highContrast, setHighContrast] = useState(false);
  const [reducedMotion, setReducedMotion] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
    setReducedMotion(mq.matches);
    mq.addEventListener('change', (e) => setReducedMotion(e.matches));
  }, []);

  useEffect(() => {
    document.body.classList.toggle('high-contrast', highContrast);
    document.body.classList.toggle('reduced-motion', reducedMotion);
  }, [highContrast, reducedMotion]);

  return (
    <AccessibilityContext.Provider value={{ highContrast, setHighContrast, reducedMotion, setReducedMotion }}>
      {children}
    </AccessibilityContext.Provider>
  );
};

export const useAccessibility = () => useContext(AccessibilityContext);
