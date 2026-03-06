import React, { useState } from 'react';
import PromptForm from '../components/PromptForm';
import CompletionList from '../components/CompletionList';

function Home() {
  const [completions, setCompletions] = useState<string[]>([]);

  const handleSubmit = async (prompt: string) => {
    const resp = await fetch(import.meta.env.VITE_BACKEND_URL + '/api/completions/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await resp.json();
    setCompletions(prev => [...prev, data.completion]);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Real‑Time Analytics Dashboard</h1>
      <PromptForm onSubmit={handleSubmit} />
      <CompletionList items={completions} />
    </div>
  );
}

export default Home;
