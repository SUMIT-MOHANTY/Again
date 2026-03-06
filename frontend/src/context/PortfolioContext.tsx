import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { PortfolioItem, FilterState, fetchPortfolio } from '../services/api';

interface PortfolioContextType {
  items: PortfolioItem[];
  loading: boolean;
  filters: FilterState;
  searchQuery: string;
  setSearchQuery: (q: string) => void;
  setFilters: (f: FilterState) => void;
}

const PortfolioContext = createContext<PortfolioContextType | null>(null);

export function PortfolioProvider({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<PortfolioItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [filters, setFilters] = useState<FilterState>({ category: '', technologies: [] });
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    setLoading(true);
    fetchPortfolio(searchQuery, filters)
      .then(setItems)
      .finally(() => setLoading(false));
  }, [searchQuery, filters]);

  return (
    <PortfolioContext.Provider value={{ items, loading, filters, searchQuery, setSearchQuery, setFilters }}>
      {children}
    </PortfolioContext.Provider>
  );
}

export function usePortfolio() {
  const ctx = useContext(PortfolioContext);
  if (!ctx) throw new Error('usePortfolio must be used within PortfolioProvider');
  return ctx;
}
