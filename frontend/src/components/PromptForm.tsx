import React, { useState } from 'react';

type Props = { onSubmit: (prompt: string) => void };

function PromptForm({ onSubmit }: Props) {
  const [value, setValue] = useState('');

  const handle = (e: React.FormEvent) => {
    e.preventDefault();
    if (value.trim()) {
      onSubmit(value.trim());
      setValue('');
    }
  };

  return (
    <form onSubmit={handle} style={{ marginBottom: '1rem' }}>
      <input
        type="text"
        value={value}
        onChange={e => setValue(e.target.value)}
        placeholder="Enter prompt..."
        style={{ width: '70%', marginRight: '0.5rem' }}
      />
      <button type="submit">Send</button>
    </form>
  );
}

export default PromptForm;
