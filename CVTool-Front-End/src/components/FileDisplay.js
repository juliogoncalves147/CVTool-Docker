import React, { useEffect, useState } from "react";
import Prism from "prismjs";
import "prismjs/components/prism-latex";
import "prismjs/themes/prism.css";
import "./FileDisplay.css";

function FileDisplay({ fileData, fileName, refreshKey }) {
  const [fileContent, setFileContent] = useState("");

  useEffect(() => {
    const fetchFileContent = async () => {
      try {
        const response = await fetch(
          `http://193.136.19.129:50760/getfile/?filename=${encodeURIComponent(
            fileName
          )}`
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
