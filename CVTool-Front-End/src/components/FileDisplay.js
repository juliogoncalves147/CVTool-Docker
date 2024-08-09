import React, { useEffect, useState } from "react";
import Prism from "prismjs";
import "prismjs/components/prism-latex";
import "prismjs/themes/prism.css";
import "./FileDisplay.css";
import { getSessionId } from "../utils/session";

export const DI = "http://193.136.19.129:50761"

export const LOCAL_HOST = "http://localhost:8000"

export const apiUrl = process.env.REACT_APP_API_URL;

function FileDisplay({ fileData, fileName, refreshKey }) {
  const [fileContent, setFileContent] = useState("");

  const sessionId = getSessionId();

  useEffect(() => {
    const fetchFileContent = async () => {
      try {
        const response = await fetch(
          apiUrl + `/getfile/?filename=${encodeURIComponent(fileName)}`,
          {
            method: 'GET',
            headers: {
              'Session-Id': sessionId
            }
          }
        );
        if (response.ok) {
          const text = await response.text();
          setFileContent(text);
        } else {
          console.error("Failed to fetch file content");
        }
      } catch (error) {
        console.error("Error fetching file:", error);
      }
    };

    fetchFileContent();
  }, [fileName, refreshKey]); // Add refreshKey to dependencies

  useEffect(() => {
    if (fileContent) {
      Prism.highlightAll();
    }
  }, [fileContent]);

  return (
    <div className="file-display">
      <pre>
        <code className="language-latex">{fileContent}</code>
      </pre>
    </div>
  );
}

export default FileDisplay;
