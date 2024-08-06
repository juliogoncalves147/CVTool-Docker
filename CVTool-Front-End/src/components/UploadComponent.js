import React from "react";
import UploadIcon from "@mui/icons-material/Upload";

function UploadComponent({ onFileUpload }) {
  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file && file.name.endsWith(".tex")) {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("http://localhost:50761/uploadfile/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        onFileUpload(data);
      } else {
        console.error("File upload failed");
      }
    } else {
      alert("Only .tex files are allowed");
    }
  };

  return (
    <div className="upload-container">
      <label className="upload-label">
        <UploadIcon />
        <input type="file" accept=".tex" onChange={handleFileChange} />
        Upload File
      </label>
    </div>
  );
}

export default UploadComponent;
