import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import SendIcon from "@mui/icons-material/Send";
import Button from "@mui/material/Button";
import { List, ListItem, ListItemText, Typography, Grid } from "@mui/material";
import ListItemIcon from "@mui/material/ListItemIcon";
import HistoryIcon from "@mui/icons-material/History";
import { getSessionId } from "../utils/session";

export const DI = "http://193.136.19.129:50761"

export const LOCAL_HOST = "http://localhost:8000"

export const apiUrl = process.env.REACT_APP_API_URL;

function QueryComponent({ onQuerySubmit, queryHistory, fileName }) {
  const [query, setQuery] = useState("");
  const [history, setHistory] = useState(queryHistory); // State for query history
  const [executingQuery, setExecutingQuery] = useState(null); // State for current executing query

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append("str_query", query);
    formData.append("filename", fileName);

    const timestamp = new Date().toLocaleTimeString([], {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
    });

    const newExecutingQuery = { status: "EXECUTING", query, timestamp };
    setExecutingQuery(newExecutingQuery);

    const sessionId = getSessionId();

    try {
      const response = await fetch(apiUrl + "/query/", {
        method: "POST",
        headers: {
          'Session-Id': sessionId
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Query submission failed");
      }

      const data = await response.json();
      const status = data.status === "OK" ? "SUCCESS" : "ERROR";
      const newQuery = { status, query: data.query, timestamp };
      onQuerySubmit(data.query);
      setHistory([newQuery, ...history]); // Prepend newQuery to history array
      setQuery("");
    } catch (error) {
      console.error("Error submitting query:", error);
      const newQuery = {
        status: "ERROR",
        query: "No file selected, please upload a valid one!",
        timestamp,
      };
      setHistory([newQuery, ...history]); // Prepend newQuery to history array
    } finally {
      setExecutingQuery(null);
    }
  };

  return (
    <div className="query-container">
      <form onSubmit={handleSubmit}>
      <TextField
  id="standard-basic"
  label="Write a new Query"
  variant="standard"
  value={query}
  onChange={(e) => setQuery(e.target.value)}
  sx={{
    '& .MuiInputLabel-root': {
      color: '#004643',  // Change the color of the label
    },
    '& .MuiInput-underline:before': {
      borderBottomColor: '#004643', // Change the default color of the underline
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: '#004643', // Change the color of the underline when focused
    },
  }}
/>

        <Button
          style={{ marginTop: "1%", backgroundColor: "#004643", color: "#FAF4D3" }}
          variant="contained"
          onClick={handleSubmit}
          type="submit"
        >
          Execute
        </Button>
      </form>
      <div className="query-history">
        <Grid container alignItems="center" spacing={1}>
          <Grid item>
            <Typography variant="h6" gutterBottom>
              Query History
            </Typography>
          </Grid>
          <Grid item>
            <HistoryIcon fontSize="medium" />
          </Grid>
        </Grid>
        <List>
          {executingQuery && (
            <ListItem key="executing" className="executing">
              <ListItemIcon>
                <SendIcon fontSize="small" />
              </ListItemIcon>
              <ListItemText
                primary={
                  <Typography variant="body2">
                    Executing query, it can take a while... -{" "}
                    {executingQuery.timestamp}
                  </Typography>
                }
              />
            </ListItem>
          )}
          {history.map((item, index) => (
            <ListItem
              key={index}
              className={item.status === "ERROR" ? "error" : "success"}
            >
              <ListItemIcon>
                <SendIcon fontSize="small" />
              </ListItemIcon>
              <ListItemText
                primary={
                  <Typography variant="body2">
                    {item.query} - {item.timestamp}
                  </Typography>
                }
              />
            </ListItem>
          ))}
        </List>
      </div>
    </div>
  );
}

export default QueryComponent;
