import React, { useState, useEffect } from "react";
import { getWorkSamples, uploadWorkSample, deleteWorkSample, WorkSample } from "../../services/api";
import WorkSampleUploadForm from "../../components/forms/WorkSampleUploadForm";

export default function WorkSamplesPage() {
  const [samples, setSamples] = useState<WorkSample[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);

  const fetchSamples = () => { getWorkSamples().then(setSamples).catch(console.error).finally(() => setLoading(false)); };
  useEffect(() => { fetchSamples(); }, []);

  const handleUpload = async (formData: FormData) => { await uploadWorkSample(formData); setShowForm(false); fetchSamples(); };
  const handleDelete = async (id: number) => { if (confirm("Delete this work sample?")) { await deleteWorkSample(id); fetchSamples(); } };

  if (loading) return <div>Loading work samples...</div>;

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
        <h2>Work Samples</h2>
        <button onClick={() => setShowForm(true)} style={{ padding: "10px 20px", background: "#4a4a4a", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" }}>+ Upload Sample</button>
      </div>

      {showForm && <div style={{ marginBottom: 30, padding: 20, background: "#fff", borderRadius: 8 }}><WorkSampleUploadForm onSubmit={handleUpload} onCancel={() => setShowForm(false)} /></div>}

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))", gap: 20 }}>
        {samples.map((s) => (
          <div key={s.id} style={{ background: "#fff", borderRadius: 8, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,0.1)" }}>
            {s.mime_type.startsWith("image/") ? (
              <img src={s.file_url} alt={s.title} style={{ width: "100%", height: 180, objectFit: "cover" }} />
            ) : (
              <div style={{ height: 180, background: "#f0f0f0", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 40 }}>📄</div>
            )}
            <div style={{ padding: 15 }}>
              <h3 style={{ margin: "0 0 5px", fontSize: 16 }}>{s.title}</h3>
              <p style={{ margin: 0, color: "#666", fontSize: 14 }}>{s.description || "No description"}</p>
              <div style={{ marginTop: 10, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <a href={s.file_url} target="_blank" rel="noopener noreferrer" style={{ color: "#0066cc", fontSize: 14 }}>View -></a>
                <button onClick={() => handleDelete(s.id)} style={{ padding: "5px 10px", background: "#e94560", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer", fontSize: 12 }}>Delete</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
