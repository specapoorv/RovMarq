import React from "react";

export default function GPSDisplay({ gpsData }){
  return (
    <div className="gps-display">
      <h3>🌍 GPS Location</h3>
      <div className="gps-info">
        <div className="gps-coordinates">
          <span className="gps-label">Current Position:</span>
          <span className="gps-value">{gpsData}</span>
        </div>
        <div className="gps-status">
          <span className="gps-indicator">●</span>
          <span>GPS Lock Active</span>
        </div>
      </div>
    </div>
  );
};