import React from 'react';
import ReactDOM from 'react-dom/client';
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import { CookiesProvider } from 'react-cookie';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';
import App from './pages/home/App';
import Articles from './pages/articles/Articles';
import Login from './pages/login/Login';

function Router() {
  return (
    <CookiesProvider>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<App />} />
          <Route exact path="/articles" element={<Articles />} />
          <Route exact path="/login" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </CookiesProvider>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router />
  </React.StrictMode>
);

reportWebVitals();
