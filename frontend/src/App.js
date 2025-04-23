import React, {useEffect, useState} from 'react';
import './App.css';

function App() {

  const [message, setmessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/")
    .then(res => res.json())
    .then(data => setmessage(data.message))
  }, [])
  
  return (
    <div className="App">
      <h1>Testing testing testing</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
