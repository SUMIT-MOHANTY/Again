import { useState, useCallback } from "react";

const useErrorHandler = () => {
  const [error, setError] = useState(null);

  const handleError = useCallback((err) => {
    const message = err?.message || err?.details?.message || "An error occurred";
    setError({ message, status: err?.status, details: err?.details });
    console.error("Error handled:", err);
  }, []);

  const clearError = useCallback(() => {
    setError(null);
  }, []);

  return { error, handleError, clearError };
};

export default useErrorHandler;
