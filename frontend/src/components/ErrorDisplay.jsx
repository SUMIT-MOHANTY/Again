import React from "react";

const ErrorDisplay = ({ error, onRetry, onDismiss }) => {
  if (!error) return null;

  const getMessage = () => {
    if (typeof error === "string") return error;
    return error.message || error.details?.message || "An error occurred";
  };

  return (
    <div style={{ padding: "16px", background: "#fee", border: "1px solid #f88", borderRadius: "4px", margin: "16px 0" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <strong style={{ color: "#c00" }}>Error:</strong> {getMessage()}
        </div>
        <div style={{ display: "flex", gap: "8px" }}>
          {onRetry && (
            <button onClick={onRetry} style={{ padding: "4px 12px" }}>
              Retry
            </button>
          )}
          {onDismiss && (
            <button onClick={onDismiss} style={{ padding: "4px 12px" }}>
              Dismiss
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default ErrorDisplay;
