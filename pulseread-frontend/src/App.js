import React from 'react';
import FileUpload from './components/FileUpload';
import SummaryList from './components/SummaryList';

function App() {
  return (
    <div>
      <h1>PulseRead</h1>
      <FileUpload />
      <SummaryList />
    </div>
  );
}

export default App;
