import React, { useState } from "react";

interface ProjectFormProps {
  initialData?: { id?: number; title: string; description: string; technologies: string[]; link: string };
  onSubmit: (data: { title: string; description: string; technologies: string[]; link: string }) => Promise<void>;
  onCancel: () => void;
}

export default function ProjectForm({ initialData, onSubmit, onCancel }: ProjectFormProps) {
  const [title, setTitle] = useState(initialData?.title || "");
  const [description, setDescription] = useState(initialData?.description || "");
  const [techStr, setTechStr] = useState(initialData?.technologies?.join(", ") || "");
  const [link, setLink] = useState(initialData?.link || "");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    if (!title.trim() || !description.trim()) { setError("Title and description required"); return; }
    setSubmitting(true);
    try {
      await onSubmit({ title: title.trim(), description: description.trim(), technologies: techStr.split(",").map((t) => t.trim()).filter(Boolean), link: link.trim() });
    } catch (err) { setError(err instanceof Error ? err.message : "Submission failed"); }
    setSubmitting(false);
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 15, maxWidth: 600 }}>
      {error && <div style={{ color: "red", padding: 10, background: "#fee", borderRadius: 4 }}>{error}</div>}
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Project Title *" maxLength={200} style={{ padding: 10, fontSize: 16 }} />
      <textarea value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description *" rows={4} style={{ padding: 10, fontSize: 16, resize: "vertical" }} />
      <input value={techStr} onChange={(e) => setTechStr(e.target.value)} placeholder="Technologies (comma-separated)" style={{ padding: 10, fontSize: 16 }} />
      <input value={link} onChange={(e) => setLink(e.target.value)} placeholder="Project URL (optional)" style={{ padding: 10, fontSize: 16 }} />
      <div style={{ display: "flex", gap: 10 }}>
        <button type="submit" disabled={submitting} style={{ padding: "10px 20px", background: "#4a4a4a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>{submitting ? "Saving..." : "Save Project"}</button>
        <button type="button" onClick={onCancel} style={{ padding: "10px 20px", background: "#999", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>Cancel</button>
      </div>
    </form>
  );
}
