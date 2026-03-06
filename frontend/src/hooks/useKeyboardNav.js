import { useCallback } from 'react';
import { handleKeyDown } from '../utils/keyboardNavigation';

export const useKeyboardNav = (handlers) => {
  return useCallback((e) => handleKeyDown(e, handlers), [handlers]);
};
