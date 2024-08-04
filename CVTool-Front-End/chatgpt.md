Sure, I can help you create a React application that matches your requirements. Let's divide the project into several components:

1. **App Component**: The main component that holds everything together.
2. **Upload Component**: Handles file uploads.
3. **FileDisplay Component**: Displays the uploaded file content.
4. **QueryComponent**: Allows the user to make queries.

Let's start with the basic structure and CSS, and then we will add the functionality to communicate with your API.

### Project Structure
```
src/
├── components/
│   ├── FileDisplay.js
│   ├── QueryComponent.js
│   └── UploadComponent.js
├── App.js
├── App.css
└── index.js
```

### 1. App Component

#### App.js
```jsx
import React, { useState } from 'react';
import UploadComponent from './components/UploadComponent';
import FileDisplay from './components/FileDisplay';
import QueryComponent from './components/QueryComponent';
import './App.css';

function App() {
  const [fileData, setFileData] = useState(null);
  const [queryHistory, setQueryHistory] = useState([]);

  const handleFileUpload = (data) => {
    setFileData(data);
  };

  const handleQuerySubmit = (query) => {
    setQueryHistory([...queryHistory, query]);
  };

  return (
    <div className="app-container">
      <div className="header">
        <button>Upload</button>
        <h1>CV Tool</h1>
        <button>Download</button>
      </div>
      <div className="content">
        <div className="left-pane">
          <QueryComponent onQuerySubmit={handleQuerySubmit} queryHistory={queryHistory} />
        </div>
        <div className="right-pane">
          <UploadComponent onFileUpload={handleFileUpload} />
          {fileData && <FileDisplay fileData={fileData} />}
        </div>
      </div>
    </div>
  );
}

export default App;
```

### 2. Upload Component

#### UploadComponent.js
```jsx
import React from 'react';

function UploadComponent({ onFileUpload }) {
  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('/uploadfile/', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        onFileUpload(data);
      } else {
        console.error('File upload failed');
      }
    }
  };

  return (
    <div className="upload-container">
      <label className="upload-label">
        <input type="file" onChange={handleFileChange} />
        Upload File
      </label>
    </div>
  );
}

export default UploadComponent;
```

### 3. FileDisplay Component

#### FileDisplay.js
```jsx
import React, { useEffect, useState } from 'react';

function FileDisplay({ fileData }) {
  const [fileContent, setFileContent] = useState('');

  useEffect(() => {
    const fetchFileContent = async () => {
      const response = await fetch('/getfile/');
      const data = await response.json();
      setFileContent(data);
    };

    fetchFileContent();
  }, [fileData]);

  return (
    <div className="file-display">
      <pre>{fileContent}</pre>
    </div>
  );
}

export default FileDisplay;
```

### 4. Query Component

#### QueryComponent.js
```jsx
import React, { useState } from 'react';

function QueryComponent({ onQuerySubmit, queryHistory }) {
  const [query, setQuery] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch('/query/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });

    if (response.ok) {
      const data = await response.json();
      onQuerySubmit(data);
      setQuery('');
    } else {
      console.error('Query submission failed');
    }
  };

  return (
    <div className="query-container">
      <form onSubmit={handleSubmit}>
        <label>Make a Query</label>
        <input 
          type="text" 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
        />
        <button type="submit">Submit</button>
      </form>
      <div className="query-history">
        <h3>Query History</h3>
        <ul>
          {queryHistory.map((query, index) => (
            <li key={index}>{query}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default QueryComponent;
```

### 5. CSS for Styling

#### App.css
```css
.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Arial, sans-serif;
}

.header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #f0f0f0;
  border-bottom: 1px solid #ccc;
}

.content {
  display: flex;
  width: 100%;
}

.left-pane, .right-pane {
  width: 50%;
  padding: 20px;
}

.upload-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  border: 2px dashed #ccc;
  margin-bottom: 20px;
  cursor: pointer;
}

.upload-label {
  cursor: pointer;
}

.upload-label input {
  display: none;
}

.file-display {
  background-color: #f9f9f9;
  padding: 20px;
  border: 1px solid #ccc;
  height: 400px;
  overflow-y: scroll;
}

.query-container {
  display: flex;
  flex-direction: column;
}

.query-container form {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.query-container input {
  margin-bottom: 10px;
  padding: 5px;
}

.query-history {
  margin-top: 20px;
}

.query-history ul {
  list-style-type: none;
  padding: 0;
}

.query-history li {
  background-color: #e0e0e0;
  margin-bottom: 5px;
  padding: 5px;
  border-radius: 3px;
}
```

### API Endpoints

Make sure your Python API has the following endpoints:

1. `POST /uploadfile/`: To handle file uploads.
2. `GET /getfile/`: To get the uploaded file's content.
3. `POST /query/`: To handle query submissions.

This setup provides a basic framework. You can expand and customize it further as per your needs. Let me know if you need any more help!