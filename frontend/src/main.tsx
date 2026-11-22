import React from 'react';
import { createRoot } from 'react-dom/client';
import AbotaApp from './app';
import './styles.css';

if ('serviceWorker' in navigator && import.meta.env.PROD) {
  window.addEventListener('load', () => void navigator.serviceWorker.register('/sw.js'));
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><AbotaApp /></React.StrictMode>);
