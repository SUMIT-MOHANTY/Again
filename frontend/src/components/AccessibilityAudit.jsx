import React, { useEffect, useState } from 'react';
import axe from 'axe-core';

export const AccessibilityAudit = ({ onComplete }) => {
  const [issues, setIssues] = useState([]);
  const [score, setScore] = useState(100);

  useEffect(() => {
    axe.run(document).then(results => {
      setIssues(results.violations);
      const passCount = results.passes.length;
      const total = passCount + results.violations.length;
      setScore(total > 0 ? Math.round((passCount / total) * 100) : 100);
      if (onComplete) onComplete(results);
    });
  }, []);

  return { issues, score };
};
