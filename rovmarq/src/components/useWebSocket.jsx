import React from "react";
import { useState } from "react";

// WebSocket Hook (simplified)
export default function useWebSocket() {
  const [connectionStatus, setConnectionStatus] = useState('Connected (Demo)');
  const [telemetryData, setTelemetryData] = useState({
    gps: '12.9716°N, 77.5946°E',
    speed: '0.0',
    battery: 85,
    signal: 75,
    altitude: '520.5'
  });

  const [scienceData, setScienceData] = useState({
    temperature: '26.5',
    humidity: '65',
    pressure: '1015.2',
    uvIndex: '5.2',
    ph: '7.1',
    conductivity: '450'
  });

  return { connectionStatus, telemetryData, scienceData };
};