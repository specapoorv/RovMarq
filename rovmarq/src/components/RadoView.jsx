import React from "react";

export default function RadoView(){
  const waypoints = [
    { lat: 12.971600, lng: 77.594600, label: 'Start Point', time: '14:30:15' },
    { lat: 12.972100, lng: 77.594800, label: 'Checkpoint 1', time: '14:32:45' },
    { lat: 12.972800, lng: 77.595200, label: 'Science Stop', time: '14:35:20' },
    { lat: 12.973500, lng: 77.595600, label: 'Waypoint A', time: '14:38:10' },
    { lat: 12.974200, lng: 77.596000, label: 'Waypoint B', time: '14:41:30' },
    { lat: 12.975000, lng: 77.596500, label: 'Current Position', time: '14:45:00' }
  ];

  return (
    <div className="rado-view">
      <div className="rado-left">
        <h3>🗺️ Mission Map</h3>
        <div className="map-placeholder">
          <div className="waypoint" style={{top: '20%', left: '30%'}}>📍 Start</div>
          <div className="waypoint" style={{top: '40%', left: '50%'}}>📍 WP-1</div>
          <div className="waypoint" style={{top: '60%', left: '70%'}}>📍 WP-2</div>
          <div className="rover-position" style={{top: '70%', left: '80%'}}>🤖</div>
        </div>
      </div>
      <div className="rado-right">
        <h3>📊 Mission GPS Log</h3>
        <div className="coordinates-list">
          {waypoints.map((coord, index) => (
            <div key={index} className="coordinate-entry">
              <div className="waypoint-label">{coord.label}</div>
              <div className="coordinate-value">{coord.lat.toFixed(6)}, {coord.lng.toFixed(6)}</div>
              <div className="timestamp">{coord.time}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};