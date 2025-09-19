import React from "react";

export default function ScienceSensors({ scienceData }){
  return (
    <div className="science-sensors">
      <h3>🔬 Science Sensors</h3>
      <div className="sensors-grid">
        <div className="sensor-item">
          <label>🌡️ Temperature:</label>
          <span>{scienceData.temperature}°C</span>
        </div>
        <div className="sensor-item">
          <label>💧 Humidity:</label>
          <span>{scienceData.humidity}%</span>
        </div>
        <div className="sensor-item">
          <label>🌬️ Air Pressure:</label>
          <span>{scienceData.pressure} hPa</span>
        </div>
        <div className="sensor-item">
          <label>☀️ UV Index:</label>
          <span>{scienceData.uvIndex}</span>
        </div>
        <div className="sensor-item">
          <label>🧪 pH Level:</label>
          <span>{scienceData.ph}</span>
        </div>
        <div className="sensor-item">
          <label>⚡ Conductivity:</label>
          <span>{scienceData.conductivity} μS/cm</span>
        </div>
      </div>
    </div>
  );
};