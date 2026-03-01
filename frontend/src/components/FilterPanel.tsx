import { FilterState } from '../services/api';

interface Props {
  categories: string[];
  technologies: string[];
  onFilterChange: (filters: FilterState) => void;
}

export function FilterPanel({ categories, technologies, onFilterChange }: Props) {
  const handleCategory = (e: React.ChangeEvent<HTMLSelectElement>) => {
    onFilterChange({ category: e.target.value, technologies: [] });
  };

  const handleTech = (tech: string, checked: boolean) => {
    const current = new Set(technologies);
    if (checked) current.add(tech);
    else current.delete(tech);
    onFilterChange({ category: '', technologies: Array.from(current) });
  };

  return (
    <div className="filter-panel">
      <select onChange={handleCategory}>
        <option value="">All Categories</option>
        {categories.map(c => <option key={c} value={c}>{c}</option>)}
      </select>
      <div className="tech-tags">
        {technologies.map(t => (
          <label key={t}>
            <input type="checkbox" onChange={e => handleTech(t, e.target.checked)} />
            {t}
          </label>
        ))}
      </div>
    </div>
  );
}
