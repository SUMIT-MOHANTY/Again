import React from "react";
import { Outlet, NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../../contexts/AuthContext";

const navItems = [
  { path: "/admin/projects", label: "Projects" },
  { path: "/admin/skills", label: "Skills" },
  { path: "/admin/work-samples", label: "Work Samples" },
];

export default function AdminLayout() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate("/login");
  };

  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>
      <aside style={{ width: 240, background: "#1a1a2e", color: "#fff", padding: 20 }}>
        <h2 style={{ marginBottom: 30 }}>Admin Panel</h2>
        <nav style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          {navItems.map((item) => (
            <NavLink key={item.path} to={item.path} style={({ isActive }) => ({ padding: "10px 15px", borderRadius: 6, background: isActive ? "#16213e" : "transparent", color: "#fff", textDecoration: "none" })}>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <button onClick={handleLogout} style={{ marginTop: 40, padding: "10px 15px", width: "100%", background: "#e94560", color: "#fff", border: "none", borderRadius: 6, cursor: "pointer" }}>Logout</button>
      </aside>
      <main style={{ flex: 1, padding: 30, background: "#f5f5f5" }}>
        <header style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 30 }}>
          <h1>Content Management</h1>
          <span style={{ color: "#666" }}>{user?.name || user?.email}</span>
        </header>
        <Outlet />
      </main>
    </div>
  );
}
