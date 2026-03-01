import { PortfolioItem } from '../services/api';

interface Props {
  item: PortfolioItem;
}

export function PortfolioCard({ item }: Props) {
  return (
    <div className="portfolio-card">
      {item.imageUrl && <img src={item.imageUrl} alt={item.title} />}
      <h3>{item.title}</h3>
      <p>{item.description.slice(0, 100)}...</p>
      <span className="category">{item.category}</span>
      <div className="techs">
        {item.technologies.map(t => <span key={t} className="tag">{t}</span>)}
      </div>
    </div>
  );
}
