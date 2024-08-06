import React, { useState, useRef } from "react";
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
import FilePresentOutlinedIcon from "@mui/icons-material/FilePresentOutlined";
import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";
import "./ToolPage.css";

function ToolPage() {
  const [fileData, setFileData] = useState(null);
  const [queryHistory, setQueryHistory] = useState([]);
  const [fileName, setFileName] = useState("");
  const [refreshKey, setRefreshKey] = useState(0);
  const fileInputRef = useRef(null);

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file && file.name.endsWith(".tex")) {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("http://0.0.0.0:5760/uploadfile/", {
        method: "POST",
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

    const response = await fetch(
      `http://0.0.0.0:5760/downloadfile/?filename=${fileName}`,
      {
        method: "GET",
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
      <Footer />
    </div>
  );
}

export default ToolPage;
