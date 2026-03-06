import { PortfolioProvider, usePortfolio } from './context/PortfolioContext';
import { SearchBar } from './components/SearchBar';
import { FilterPanel } from './components/FilterPanel';
import { PortfolioGrid } from './components/PortfolioGrid';

const CATEGORIES = ['Web Development', 'Mobile App', 'Data Science', 'DevOps'];
const TECHNOLOGIES = ['React', 'Python', 'TypeScript', 'PostgreSQL', 'Docker', 'AWS', 'Node.js', 'Vue.js'];

function AppContent() {
  const { items, loading, setSearchQuery, setFilters } = usePortfolio();
  return (
    <div className="app">
      <h1>Portfolio Projects</h1>
      <SearchBar onSearch={setSearchQuery} />
      <FilterPanel categories={CATEGORIES} technologies={TECHNOLOGIES} onFilterChange={setFilters} />
      {loading ? <p>Loading...</p> : <PortfolioGrid items={items} />}
    </div>
  );
}

export default function App() {
  return (
    <PortfolioProvider>
      <AppContent />
    </PortfolioProvider>
  );
}
