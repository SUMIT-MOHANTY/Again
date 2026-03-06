import React, { ReactNode } from 'react';
import './Layout.css';

type Props = { children: ReactNode };

export default function Layout({ children }: Props) {
  return (
    <div className="layout">
      <header className="header">AI Prompt Service</header>
      <main className="content">{children}</main>
    </div>
  );
}
