import { Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Layout from './components/Layout';

function App() {
  const isAuth = false; // placeholder auth state
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={isAuth ? <Dashboard /> : <Navigate to="/login" replace />} />
      </Routes>
    </Layout>
  );
}

export default App;
