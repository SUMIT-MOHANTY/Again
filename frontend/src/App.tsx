import React, { useState } from 'react';
import axios from 'axios';
function App() {
  const [data, setData] = useState(null);
  const fetchData = async () => {
    const res = await axios.get('/v1/external-data');
    setData(res.data);
  };
  return (
    <div>
      <h1>Resilient Frontend</h1>
      <button onClick={fetchData}>Get Data</button>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
export default App;
