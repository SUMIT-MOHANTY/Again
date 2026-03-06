export interface PortfolioItem {
  id: number;
  title: string;
  description: string;
  category: string;
  technologies: string[];
  imageUrl?: string;
  projectUrl?: string;
}

export interface FilterState {
  category: string;
  technologies: string[];
}

const API_BASE = '/api';

export async function fetchPortfolio(query: string = '', filters: FilterState): Promise<PortfolioItem[]> {
  const params = new URLSearchParams();
  if (query) params.set('q', query);
  if (filters.category) params.set('category', filters.category);
  if (filters.technologies.length) params.set('tags', filters.technologies.join(','));
  const res = await fetch(`${API_BASE}/portfolio?${params}`);
  const data = await res.json();
  return data.items;
}
