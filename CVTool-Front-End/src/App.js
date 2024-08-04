import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import ToolPage from "./pages/ToolPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/tool" element={<ToolPage />} />
      </Routes>
    </Router>
  );
}

export default App;
