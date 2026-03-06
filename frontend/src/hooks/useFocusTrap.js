import { useEffect } from 'react';
import { trapFocus } from '../utils/focusManager';

export const useFocusTrap = (containerRef, isActive) => {
  useEffect(() => {
    if (!isActive || !containerRef.current) return;
    return trapFocus(containerRef.current);
  }, [isActive, containerRef]);
};
