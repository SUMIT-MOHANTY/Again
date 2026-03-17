let savedFocus = null;

export const saveFocus = () => { savedFocus = document.activeElement; };

export const restoreFocus = () => { savedFocus?.focus(); savedFocus = null; };

export const trapFocus = (container) => {
  const focusable = container?.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
  if (!focusable?.length) return;
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  const handler = (e) => {
    if (e.key !== 'Tab') return;
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  };
  container?.addEventListener('keydown', handler);
  return () => container?.removeEventListener('keydown', handler);
};
