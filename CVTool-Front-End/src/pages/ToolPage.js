import React, { useState, useRef } from "react";
import HelpOutlineIcon from "@mui/icons-material/HelpOutline"; // White question mark icon
import NoteIcon from "@mui/icons-material/Note";
import CloseIcon from "@mui/icons-material/Close";
import { Paper } from "@mui/material";
import { Link } from "react-router-dom";
import UploadComponent from "../components/UploadComponent";
import FileDisplay from "../components/FileDisplay";
import QueryComponent from "../components/QueryComponent";
import Footer from "../components/Footer";
import Button from "@mui/material/Button";
import UploadIcon from "@mui/icons-material/Upload";
import DownloadIcon from "@mui/icons-material/Download";
import RefreshIcon from "@mui/icons-material/Refresh";
import HomeIcon from "@mui/icons-material/Home";
import { Typography , IconButton} from "@mui/material";
import { getSessionId } from "../utils/session";
import FilePresentOutlinedIcon from "@mui/icons-material/FilePresentOutlined";
import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";
import "./ToolPage.css";

export const DI = "http://193.136.19.129:50761"

export const LOCAL_HOST = "http://localhost:8000"

export const apiUrl = process.env.REACT_APP_API_URL;

function ToolPage() {
  const [fileData, setFileData] = useState(null);
  const [queryHistory, setQueryHistory] = useState([]);
  const [fileName, setFileName] = useState("");
  const [refreshKey, setRefreshKey] = useState(0);
  const fileInputRef = useRef(null);
  const [isSuggestionBoxOpen, setSuggestionBoxOpen] = useState(false);

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
        setFileData(data.processed_file_path);
        setFileName(data.original_filename);
      } else {
        console.error("File upload failed");
      }
    } else {
      alert("Only .tex files are allowed");
    }
  };

  const handleDownloadClick = async () => {
    if (!fileData) {
      alert("No file to download");
      return;
    }
    const sessionId = getSessionId();
    
    const response = await fetch(
      apiUrl + `/downloadfile/?filename=${fileName}`,
      {
        method: "GET",
        headers: {
          'Session-Id': sessionId
        }  
      }
    );

    if (response.ok) {
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = fileName;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    } else {
      console.error("File download failed");
    }
  };

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleFileUpload = (data) => {
    setFileData(data.processed_file_path);
    setFileName(data.original_filename);
  };

  const handleQuerySubmit = (query) => {
    setQueryHistory([...queryHistory, query]);
  };

  const handleRefreshClick = () => {
    setRefreshKey((prevKey) => prevKey + 1);
  };

  const toggleSuggestionBox = () => {
    setSuggestionBoxOpen(!isSuggestionBoxOpen);
  };

  return (
    <div className="app-container">
      <div className="navbar">
        <Button
          style={{ backgroundColor: "#ffffff" }}
          variant="outlined"
          startIcon={<UploadIcon />}
          onClick={handleUploadClick}
        >
          Upload
        </Button>
        <div className="navbar-content">
        <h1 className="navbar-title">Resume Management Tool for LaTeX</h1>
        <IconButton
          component={Link}
          to="/"
          style={{ color: '#ffffff', marginLeft: 'auto' }}
          aria-label="home">
          <HomeIcon />
        </IconButton>
      </div>
        <Button
          style={{ backgroundColor: "#ffffff" }}
          variant="outlined"
          startIcon={<DownloadIcon />}
          onClick={handleDownloadClick}
          disabled={!fileData}
        >
          Download
        </Button>
      </div>
      <input
        type="file"
        accept=".tex"
        ref={fileInputRef}
        style={{ display: "none" }}
        onChange={handleFileChange}
      />
      <div className="content">
        <div className="left-pane">
          <QueryComponent
            onQuerySubmit={handleQuerySubmit}
            queryHistory={queryHistory}
            fileName={fileName}
          />
        </div>
        <div className="right-pane">
          {!fileData ? (
            <UploadComponent onFileUpload={handleFileUpload} />
          ) : (
            <div>
              <div className="file-header">
                <div className="file-name">
                  <FilePresentOutlinedIcon />
                  <Typography variant="h6" className="file-name-text">
                    {fileName}
                  </Typography>
                </div>
                <Button
                  style={{ marginLeft: "10px" }}
                  variant="contained"
                  startIcon={<RefreshIcon />}
                  onClick={handleRefreshClick}
                >
                  Refresh
                </Button>
              </div>
              <FileDisplay
                fileData={fileData}
                fileName={fileName}
                refreshKey={refreshKey}
              />
            </div>
          )}
        </div>
      </div>
      <IconButton
        className="help-icon"
        onClick={toggleSuggestionBox}
        style={{
          position: "fixed",
          bottom: "35px",
          left: "25px", // Position it to the left bottom corner
          backgroundColor: "#007bff", // Blue background
          color: "#ffffff", // White icon
          zIndex: 1000,
        }}
      >
        <HelpOutlineIcon />
        {isSuggestionBoxOpen && (
        <Paper
          elevation={3}
          className="suggestion-box"
          style={{
            position: "fixed",
            bottom: "80px",
            left: "20px", // Align with the help icon on the left
            width: "50%",
            padding: "15px",
            backgroundColor: "#295F98", // Blue background for the suggestion box
            color: "#ffffff", // White text for the suggestion box
            zIndex: 1000,
          }}
        >
          <div style={{ position: "relative", textAlign: "center" }}>
  <Typography variant="h6">Query Suggestions</Typography>
  <IconButton
    onClick={toggleSuggestionBox}
    style={{
      position: "absolute",   // Absolute positioning
      right: 0,               // Align to the right
      top: 0,                 // Align to the top
      padding: 0,
      color: "#ffffff"
    }}
  >
    <CloseIcon />
  </IconButton>
</div>
          <ul>
            <li>
              <Typography variant="body2">
                <strong>Show</strong> * <strong> Filtered By </strong> subsectionsection = 'Chair Person' and date > '2010'
              </Typography>
            </li>
            <li>
              <Typography variant="body1">
              <strong>Show</strong> * <strong> Filtered By </strong> section != 'Work experience' and date = '2010'
              </Typography>
            </li>
            <li>
              <Typography variant="body1">
                <strong>Translate from</strong> 'fr' <strong> TO </strong> 'en'
              </Typography>
            </li>
            <li>
              <Typography variant="body1">
                <strong>Reorder</strong> 'Work experience', 'Education and training', 'Soft Skills'
              </Typography>
            </li>
            {/* Add more suggestions here */}
          </ul>
        </Paper>
      )}

      </IconButton>
      <Footer />
    </div>
  );
}

export default ToolPage;
