import { PortfolioItem } from '../services/api';
import { PortfolioCard } from './PortfolioCard';

interface Props {
  items: PortfolioItem[];
}

export function PortfolioGrid({ items }: Props) {
  if (!items.length) return <p className="no-results">No projects found.</p>;
  return (
    <div className="portfolio-grid">
      {items.map(item => <PortfolioCard key={item.id} item={item} />)}
    </div>
  );
}
