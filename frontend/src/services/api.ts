const API_BASE = "/api";

const getHeaders = () => {
  const token = localStorage.getItem("token");
  return token ? { Authorization: `Bearer ${token}` } : {};
};

async function handleResponse<T>(res: Response): Promise<T> {
  if (!res.ok) {
    const err = await res.json().catch(() => ({ message: "Request failed" }));
    throw new Error(err.message || "Request failed");
  }
  return res.json();
}

// Auth
export const login = async (email: string, password: string) => {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  const data = await handleResponse<{ access_token: string }>();
  localStorage.setItem("token", data.access_token);
  return getCurrentUser();
};

export const logout = async () => {
  await fetch(`${API_BASE}/auth/logout`, { method: "POST", headers: getHeaders() });
  localStorage.removeItem("token");
};

export const getCurrentUser = async () => {
  const res = await fetch(`${API_BASE}/auth/me`, { headers: getHeaders() });
  if (!res.ok) return null;
  return res.json();
};

// Projects
interface Project { id: number; title: string; description: string; technologies: string[]; link: string | null; created_at: string; updated_at: string; }

export const getProjects = async () => handleResponse<Project[]>(await fetch(`${API_BASE}/projects`, { headers: getHeaders() }));
export const getProject = async (id: number) => handleResponse<Project>(await fetch(`${API_BASE}/projects/${id}`, { headers: getHeaders() }));
export const createProject = async (data: Partial<Project>) => handleResponse<Project>(await fetch(`${API_BASE}/projects`, { method: "POST", headers: { "Content-Type": "application/json", ...getHeaders() }, body: JSON.stringify(data) }));
export const updateProject = async (id: number, data: Partial<Project>) => handleResponse<Project>(await fetch(`${API_BASE}/projects/${id}`, { method: "PUT", headers: { "Content-Type": "application/json", ...getHeaders() }, body: JSON.stringify(data) }));
export const deleteProject = async (id: number) => { await fetch(`${API_BASE}/projects/${id}`, { method: "DELETE", headers: getHeaders() }); };

// Skills
interface Skill { id: number; name: string; category: string; proficiency: number; created_at: string; }

export const getSkills = async () => handleResponse<Skill[]>(await fetch(`${API_BASE}/skills`, { headers: getHeaders() }));
export const createSkill = async (data: Partial<Skill>) => handleResponse<Skill>(await fetch(`${API_BASE}/skills`, { method: "POST", headers: { "Content-Type": "application/json", ...getHeaders() }, body: JSON.stringify(data) }));
export const updateSkill = async (id: number, data: Partial<Skill>) => handleResponse<Skill>(await fetch(`${API_BASE}/skills/${id}`, { method: "PUT", headers: { "Content-Type": "application/json", ...getHeaders() }, body: JSON.stringify(data) }));
export const deleteSkill = async (id: number) => { await fetch(`${API_BASE}/skills/${id}`, { method: "DELETE", headers: getHeaders() }); };

// Work Samples
interface WorkSample { id: number; title: string; description: string; file_url: string; mime_type: string; created_at: string; }

export const getWorkSamples = async () => handleResponse<WorkSample[]>(await fetch(`${API_BASE}/work-samples`, { headers: getHeaders() }));
export const uploadWorkSample = async (formData: FormData) => handleResponse<WorkSample>(await fetch(`${API_BASE}/work-samples`, { method: "POST", headers: getHeaders(), body: formData }));
export const deleteWorkSample = async (id: number) => { await fetch(`${API_BASE}/work-samples/${id}`, { method: "DELETE", headers: getHeaders() }); };
