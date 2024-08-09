import React from "react";
import UploadIcon from "@mui/icons-material/Upload";
import { getSessionId } from "../utils/session";


export const DI = "http://193.136.19.129:50761"

export const LOCAL_HOST = "http://localhost:8000"

export const apiUrl = process.env.REACT_APP_API_URL;

function UploadComponent({ onFileUpload }) {
  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file && file.name.endsWith(".tex")) {
      const formData = new FormData();
      formData.append("file", file);

      const sessionId = getSessionId();

      const response = await fetch(apiUrl + "/uploadfile/", {
        method: "POST",
        headers: {
          'Session-Id': sessionId
        },
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
