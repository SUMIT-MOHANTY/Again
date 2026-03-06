export const handleKeyDown = (e, actions) => {
  const { key, shiftKey } = e;
  const keyActions = {
    Enter: actions.onEnter,
    Escape: actions.onEscape,
    ArrowUp: actions.onArrowUp,
    ArrowDown: actions.onArrowDown,
    ArrowLeft: actions.onArrowLeft,
    ArrowRight: actions.onArrowRight,
    Tab: shiftKey ? actions.onShiftTab : actions.onTab,
  };
  if (keyActions[key]) {
    e.preventDefault();
    keyActions[key]?.(e);
  }
};

export const getFocusableElements = (container) =>
  container?.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
