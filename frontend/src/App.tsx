import React, { useEffect, useState } from 'react';

function App() {
  const [msg, setMsg] = useState('Loading...');
  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(r => r.text())
      .then(text => setMsg(text))
      .catch(() => setMsg('Backend unreachable'));
  }, []);
  return <div style={{fontFamily: 'sans-serif', padding: '2rem'}}>{msg}</div>;
}

export default App;
