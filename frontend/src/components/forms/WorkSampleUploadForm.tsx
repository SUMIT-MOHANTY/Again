import React, { useState } from "react";

interface WorkSampleUploadFormProps {
  onSubmit: (data: FormData) => Promise<void>;
  onCancel: () => void;
}

export default function WorkSampleUploadForm({ onSubmit, onCancel }: WorkSampleUploadFormProps) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    if (!title.trim()) { setError("Title required"); return; }
    if (!file) { setError("File required"); return; }
    if (file.size > 10 * 1024 * 1024) { setError("File too large (max 10MB)"); return; }
    const formData = new FormData();
    formData.append("title", title.trim());
    formData.append("description", description.trim());
    formData.append("file", file);
    setSubmitting(true);
    try { await onSubmit(formData); } catch (err) { setError(err instanceof Error ? err.message : "Upload failed"); }
    setSubmitting(false);
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 15, maxWidth: 500 }}>
      {error && <div style={{ color: "red", padding: 10, background: "#fee", borderRadius: 4 }}>{error}</div>}
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title *" maxLength={200} style={{ padding: 10, fontSize: 16 }} />
      <textarea value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description (optional)" rows={3} style={{ padding: 10, fontSize: 16, resize: "vertical" }} />
      <input type="file" accept="image/*,application/pdf" onChange={(e) => setFile(e.target.files?.[0] || null)} style={{ padding: 10 }} />
      {file && <div style={{ fontSize: 14, color: "#666" }}>Selected: {file.name} ({(file.size / 1024).toFixed(1)} KB)</div>}
      <div style={{ display: "flex", gap: 10 }}>
        <button type="submit" disabled={submitting} style={{ padding: "10px 20px", background: "#4a4a4a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>{submitting ? "Uploading..." : "Upload Sample"}</button>
        <button type="button" onClick={onCancel} style={{ padding: "10px 20px", background: "#999", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>Cancel</button>
      </div>
    </form>
  );
}
