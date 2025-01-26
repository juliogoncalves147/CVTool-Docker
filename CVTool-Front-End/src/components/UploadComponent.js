import React from "react";
import UploadIcon from "@mui/icons-material/Upload";
import { getSessionId } from "../utils/session";
import styled from "styled-components";

// Define the API URLs
export const DI = "http://193.136.19.129:50761";
export const LOCAL_HOST = "http://localhost:8000";
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
          'Session-Id': sessionId,
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
    <UploadContainer>
      <UploadLabel>
        <UploadIcon />
        <input type="file" accept=".tex" onChange={handleFileChange} />
        Upload File
      </UploadLabel>
    </UploadContainer>
  );
}

export default UploadComponent;

// Styled components
const UploadContainer = styled.div`
  display: flex;                /* Enable Flexbox */
  justify-content: center;      /* Center content horizontally */
  align-items: center;          /* Center content vertically */
  height: 100vh;                /* Make the container take full viewport height */
  width: 100%;                  /* Make the container full width */
`;

const UploadLabel = styled.label`
  display: flex;                /* Flexbox for label to align icon and text */
  align-items: center;          /* Vertically align the icon and text */
  cursor: pointer;             /* Make the label look like a button */
  padding: 10px 20px;           /* Add padding for a button-like appearance */
  background-color: #004643;    /* Background color for the label (optional) */
  color: #FAF4D3;               /* Text color (optional) */
  border: 2px solid #004643;    /* Border color (optional) */
  border-radius: 4px;           /* Optional: rounded corners */

  input {
    display: none;              /* Hide the default file input */
  }

  svg {
    margin-right: 8px;          /* Add space between the icon and text */
  }
`;
