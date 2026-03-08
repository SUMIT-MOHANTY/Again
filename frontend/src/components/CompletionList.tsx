import React from 'react';

type Props = { items: string[] };

function CompletionList({ items }: Props) {
  return (
    <ul>
      {items.map((c, i) => (
        <li key={i}>{c}</li>
      ))}
    </ul>
  );
}

export default CompletionList;
