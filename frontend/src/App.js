import React, {useEffect, useState} from 'react';
import axios from 'axios';
function App(){
  const [backups, setBackups] = useState([]);
  useEffect(()=>{axios.get('/api/v1/backups').then(r=>setBackups(r.data));}, []);
  const trigger = ()=>{axios.post('/api/v1/backups').then(()=>window.location.reload());};
  return (<div style={{padding:'2rem'}}>
    <h1>PostgreSQL Backups</h1>
    <button onClick={trigger}>Run Backup Now</button>
    <ul>{backups.map(b=>(<li key={b.id}>{b.filename} - {b.size_bytes} bytes - {b.created_at}</li>))}</ul>
  </div>);
}
export default App;
