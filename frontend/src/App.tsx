import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import AdminLayout from "./components/layout/AdminLayout";
import PrivateRoute from "./components/common/PrivateRoute";
import ProjectsPage from "./pages/admin/ProjectsPage";
import SkillsPage from "./pages/admin/SkillsPage";
import WorkSamplesPage from "./pages/admin/WorkSamplesPage";
import LoginPage from "./pages/admin/LoginPage";

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/admin" element={<PrivateRoute><AdminLayout /></PrivateRoute>}>
            <Route index element={<Navigate to="/admin/projects" replace />} />
            <Route path="projects" element={<ProjectsPage />} />
            <Route path="skills" element={<SkillsPage />} />
            <Route path="work-samples" element={<WorkSamplesPage />} />
          </Route>
          <Route path="*" element={<Navigate to="/admin/projects" replace />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
