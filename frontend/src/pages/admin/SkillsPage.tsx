import React, { useState, useEffect } from "react";
import { getSkills, createSkill, updateSkill, deleteSkill, Skill } from "../../services/api";
import SkillForm from "../../components/forms/SkillForm";

export default function SkillsPage() {
  const [skills, setSkills] = useState<Skill[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingSkill, setEditingSkill] = useState<Skill | null>(null);

  const fetchSkills = () => { getSkills().then(setSkills).catch(console.error).finally(() => setLoading(false)); };
  useEffect(() => { fetchSkills(); }, []);

  const handleCreate = async (data: Partial<Skill>) => { await createSkill(data); setShowForm(false); fetchSkills(); };
  const handleUpdate = async (data: Partial<Skill>) => { if (editingSkill) { await updateSkill(editingSkill.id, data); setEditingSkill(null); fetchSkills(); } };
  const handleDelete = async (id: number) => { if (confirm("Delete this skill?")) { await deleteSkill(id); fetchSkills(); } };

  if (loading) return <div>Loading skills...</div>;

  const categories = ["frontend", "backend", "tools", "other"];

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
        <h2>Skills</h2>
        <button onClick={() => setShowForm(true)} style={{ padding: "10px 20px", background: "#4a4a4a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>+ Add Skill</button>
      </div>

      {showForm && <div style={{ marginBottom: 30, padding: 20, background: "#fff", borderRadius: 8 }}><SkillForm onSubmit={handleCreate} onCancel={() => setShowForm(false)} /></div>}
      {editingSkill && (
        <div style={{ marginBottom: 30, padding: 20, background: "#fff", borderRadius: 8 }}>
          <h3>Edit Skill</h3>
          <SkillForm initialData={editingSkill} onSubmit={handleUpdate} onCancel={() => setEditingSkill(null)} />
        </div>
      )}

      {categories.map((cat) => {
        const catSkills = skills.filter((s) => s.category === cat);
        if (!catSkills.length) return null;
        return (
          <div key={cat} style={{ marginBottom: 25 }}>
            <h3 style={{ textTransform: "capitalize", marginBottom: 10 }}>{cat}</h3>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))", gap: 15 }}>
              {catSkills.map((s) => (
                <div key={s.id} style={{ padding: 15, background: "#fff", borderRadius: 8, boxShadow: "0 1px 3px rgba(0,0,0,0.1)" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
                    <span style={{ fontWeight: 500 }}>{s.name}</span>
                    <div style={{ display: "flex", gap: 5 }}>
                      <button onClick={() => setEditingSkill(s)} style={{ padding: "3px 8px", background: "#0066cc", color: "#fff", border: "none", borderRadius: 3, cursor: "pointer", fontSize: 12 }}>Edit</button>
                      <button onClick={() => handleDelete(s.id)} style={{ padding: "3px 8px", background: "#e94560", color: "#fff", border: "none", borderRadius: 3, cursor: "pointer", fontSize: 12 }}>×</button>
                    </div>
                  </div>
                  <div style={{ background: "#e0e0e0", borderRadius: 4, height: 8, overflow: "hidden" }}>
                    <div style={{ width: `${s.proficiency}%`, background: "#4a4a4a", height: "100%" }} />
                  </div>
                  <div style={{ textAlign: "right", fontSize: 12, color: "#666", marginTop: 4 }}>{s.proficiency}%</div>
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}
