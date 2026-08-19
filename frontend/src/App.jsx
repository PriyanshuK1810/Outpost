import { useState, useEffect } from "react";
import apiClient from "./api/client";

function App(){
  const [status, setStatus] = useState("Loading...");

  useEffect(() => {
    apiClient.get("/health").then((response) => {
      setStatus(response.data.status);
    });
  }, []);
  return <div>Backend Status: {status}</div>;
}

export default App
