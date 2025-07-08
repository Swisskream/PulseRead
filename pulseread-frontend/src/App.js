import React, {useState, useEffect} from 'react';
import FileUpload from './components/FileUpload';
import SummaryList from './components/SummaryList';
import './stylesheets/app.css';

function App() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    document.documentElement.setAttribute(
      'data-theme',
      darkMode ? 'dark' : 'light'
    );
  }, [darkMode]);

  return (
    <div className='App'>
      <div className='theme-toggle'>
        <button onClick={() => setDarkMode(!darkMode)}>
          Toggle {darkMode ? 'Light' : 'Dark'} Mode
        </button>
      </div>
      
      <h1 className='app-title'>PulseRead</h1>
      <p className='app-tagline'>AI-powered insights from your users, delivered in real time.</p>

      <FileUpload />
      <SummaryList />
    </div>
  );
}

export default App;
