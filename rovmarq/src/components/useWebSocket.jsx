import { useState, useEffect } from "react";

export default function useWebSocket() {
  const [connectionStatus, setConnectionStatus] = useState("Disconnected");
  const [data, setData] = useState(null); // single topic data

  useEffect(() => {
  const ws = new WebSocket("ws://127.0.0.1:8080");

    ws.onopen = () => setConnectionStatus("Connected");
    ws.onclose = () => setConnectionStatus("Disconnected");

    ws.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data);
        // Only one topic, so we just store msg.data
        setData(msg);
      } catch (err) {
        console.error("Failed to parse WebSocket message:", err);
      }
    };

    return () => ws.close();
  }, []);

  return { connectionStatus, data };
}

