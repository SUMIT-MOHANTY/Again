import React, { useState, useEffect } from "react";
import { getProjects, createProject, updateProject, deleteProject, Project } from "../../services/api";
import ProjectForm from "../../components/forms/ProjectForm";

export default function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingProject, setEditingProject] = useState<Project | null>(null);

  const fetchProjects = () => { getProjects().then(setProjects).catch(console.error).finally(() => setLoading(false)); };
  useEffect(() => { fetchProjects(); }, []);

  const handleCreate = async (data: Partial<Project>) => { await createProject(data); setShowForm(false); fetchProjects(); };
  const handleUpdate = async (data: Partial<Project>) => { if (editingProject) { await updateProject(editingProject.id, data); setEditingProject(null); fetchProjects(); } };
  const handleDelete = async (id: number) => { if (confirm("Delete this project?")) { await deleteProject(id); fetchProjects(); } };

  if (loading) return <div>Loading projects...</div>;

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
        <h2>Projects</h2>
        <button onClick={() => setShowForm(true)} style={{ padding: "10px 20px", background: "#4a4a4a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>+ Add Project</button>
      </div>

      {showForm && <div style={{ marginBottom: 30, padding: 20, background: "#fff", borderRadius: 8 }}><ProjectForm onSubmit={handleCreate} onCancel={() => setShowForm(false)} /></div>}
      {editingProject && (
        <div style={{ marginBottom: 30, padding: 20, background: "#fff", borderRadius: 8 }}>
          <h3>Edit Project</h3>
          <ProjectForm initialData={editingProject} onSubmit={handleUpdate} onCancel={() => setEditingProject(null)} />
        </div>
      )}

      <div style={{ display: "flex", flexDirection: "column", gap: 15 }}>
        {projects.map((p) => (
          <div key={p.id} style={{ padding: 20, background: "#fff", borderRadius: 8, boxShadow: "0 1px 3px rgba(0,0,0,0.1)" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
              <div>
                <h3 style={{ margin: "0 0 5px" }}>{p.title}</h3>
                <p style={{ margin: 0, color: "#666" }}>{p.description}</p>
                <div style={{ marginTop: 10, display: "flex", gap: 5, flexWrap: "wrap" }}>
                  {p.technologies.map((t, i) => <span key={i} style={{ padding: "2px 8px", background: "#e0e0e0", borderRadius: 4, fontSize: 12 }}>{t}</span>)}
                </div>
                {p.link && <a href={p.link} target="_blank" rel="noopener noreferrer" style={{ display: "inline-block", marginTop: 10, color: "#0066cc" }}>View Project -></a>}
              </div>
              <div style={{ display: "flex", gap: 10 }}>
                <button onClick={() => setEditingProject(p)} style={{ padding: "5px 10px", background: "#0066cc", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>Edit</button>
                <button onClick={() => handleDelete(p.id)} style={{ padding: "5px 10px", background: "#e94560", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>Delete</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
