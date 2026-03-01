import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../../contexts/AuthContext";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const from = (location.state as { from?: { pathname: string } })?.from?.pathname || "/admin/projects";

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    if (!email || !password) { setError("Please enter email and password"); return; }
    setLoading(true);
    try { await login(email, password); navigate(from, { replace: true }); } catch (err) { setError(err instanceof Error ? err.message : "Login failed"); }
    setLoading(false);
  };

  return (
    <div style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", background: "#f5f5f5" }}>
      <div style={{ padding: 40, background: "#fff", borderRadius: 8, boxShadow: "0 2px 10px rgba(0,0,0,0.1)", width: 360 }}>
        <h2 style={{ marginTop: 0, textAlign: "center" }}>Admin Login</h2>
        {error && <div style={{ color: "red", padding: 10, background: "#fee", borderRadius: 4, marginBottom: 15 }}>{error}</div>}
        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 15 }}>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" style={{ padding: 12, fontSize: 16 }} />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" style={{ padding: 12, fontSize: 16 }} />
          <button type="submit" disabled={loading} style={{ padding: 12, fontSize: 16, background: "#4a4a4a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>{loading ? "Logging in..." : "Login"}</button>
        </form>
      </div>
    </div>
  );
}
