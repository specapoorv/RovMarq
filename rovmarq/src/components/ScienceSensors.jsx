import React from "react";

export default function ScienceSensors({ scienceData }) {
  if (!scienceData) {
    return <p>Waiting for data...</p>;
  }

  // scienceData looks like: { topic: "/chatter", data: ... }
  const d = scienceData.data;

  // If data is just a string, show it raw
  if (typeof d === "string") {
    return (
      <div className="science-sensors">
        <h3>🔬 Science Sensors</h3>
        <p>Raw data: {d}</p>
      </div>
    );
  }

  // Otherwise assume it's an object with sensor fields
  return (
    <div className="science-sensors">
      <h3>🔬 Science Sensors</h3>
      <div className="sensors-grid">
        <div className="sensor-item">
          <label>🌡️ Temperature:</label>
          <span>{d.temperature ?? "--"}°C</span>
        </div>
        <div className="sensor-item">
          <label>💧 Humidity:</label>
          <span>{d.humidity ?? "--"}%</span>
        </div>
        <div className="sensor-item">
          <label>🌬️ Air Pressure:</label>
          <span>{d.pressure ?? "--"} hPa</span>
        </div>
        <div className="sensor-item">
          <label>☀️ UV Index:</label>
          <span>{d.uvIndex ?? "--"}</span>
        </div>
        <div className="sensor-item">
          <label>🧪 pH Level:</label>
          <span>{d.ph ?? "--"}</span>
        </div>
        <div className="sensor-item">
          <label>⚡ Conductivity:</label>
          <span>{d.conductivity ?? "--"} μS/cm</span>
        </div>
      </div>
    </div>
  );
}
