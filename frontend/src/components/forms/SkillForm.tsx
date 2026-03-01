import React, { useState } from "react";

interface SkillFormProps {
  initialData?: { id?: number; name: string; category: string; proficiency: number };
  onSubmit: (data: { name: string; category: string; proficiency: number }) => Promise<void>;
  onCancel: () => void;
}

const CATEGORIES = ["frontend", "backend", "tools", "other"];

export default function SkillForm({ initialData, onSubmit, onCancel }: SkillFormProps) {
  const [name, setName] = useState(initialData?.name || "");
  const [category, setCategory] = useState(initialData?.category || "frontend");
  const [proficiency, setProficiency] = useState(initialData?.proficiency || 50);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    if (!name.trim()) { setError("Skill name required"); return; }
    setSubmitting(true);
    try { await onSubmit({ name: name.trim(), category, proficiency }); } catch (err) { setError(err instanceof Error ? err.message : "Submission failed"); }
    setSubmitting(false);
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 15, maxWidth: 400 }}>
      {error && <div style={{ color: "red", padding: 10, background: "#fee", borderRadius: 4 }}>{error}</div>}
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Skill Name *" maxLength={100} style={{ padding: 10, fontSize: 16 }} />
      <select value={category} onChange={(e) => setCategory(e.target.value)} style={{ padding: 10, fontSize: 16 }}>
        {CATEGORIES.map((c) => <option key={c} value={c}>{c.charAt(0).toUpperCase() + c.slice(1)}</option>)}
      </select>
      <div style={{ display: "flex", flexDirection: "column", gap: 5 }}>
        <label>Proficiency: {proficiency}%</label>
        <input type="range" min={1} max={100} value={proficiency} onChange={(e) => setProficiency(Number(e.target.value))} />
      </div>
      <div style={{ display: "flex", gap: 10 }}>
        <button type="submit" disabled={submitting} style={{ padding: "10px 20px", background: "#4a4a4a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>{submitting ? "Saving..." : "Save Skill"}</button>
        <button type="button" onClick={onCancel} style={{ padding: "10px 20px", background: "#999", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>Cancel</button>
      </div>
    </form>
  );
}
