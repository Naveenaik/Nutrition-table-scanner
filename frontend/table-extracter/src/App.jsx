import  { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [imageSrc, setImageSrc] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setImageSrc(`data:image/png;base64,${response.data.plot_url}`);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div className="App">
      <h1>Upload an Image</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload and Process</button>
      {imageSrc && <img src={imageSrc} alt="Processed Result" />}
    </div>
  );
}

export default App;
