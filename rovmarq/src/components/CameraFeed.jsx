import React from "react";
import '../App.css';

// Simple Components
export default function CameraFeed({ title, feedId }) {
  return (
    <div className="camera-feed">
      <h3>{title}</h3>
      <div className="camera-display">
        <p>Camera Feed {feedId}</p>
        <p>📹 Live Stream</p>
      </div>
    </div>
  );
};