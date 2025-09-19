import React, { useState, useEffect } from 'react';
import logo from './Anveshak.png';
import './App.css';
import CameraFeed from './components/CameraFeed';
import GPSDisplay from './components/GPSDisplay';
import ScienceSensors from './components/ScienceSensors';
import RadoView from './components/RadoView';
import useWebSocket from './components/useWebSocket';

// Main App Component
const App = () => {
  const [activeView, setActiveView] = useState('cameras');
  const { connectionStatus, telemetryData, scienceData } = useWebSocket();

  const handleEmergencyStop = () => {
    console.log('🚨 EMERGENCY STOP ACTIVATED!');
  };

  return (
    <div className="app">
      {/* Header */}
      <header className="app-header">
        <div className="header-left">
          <img 
            src={logo}
            alt="Team Logo" 
            className="team-logo"
            onError={(e) => {
              e.target.style.display = 'none';
              e.target.nextSibling.style.display = 'inline';
            }}
          />
          <span className="logo-fallback" style={{display: 'none'}}>🏆</span>
          <h1>Rover Control Interface</h1>
        </div>
        <div className="connection-status">
          Status: <span className="connected">{connectionStatus}</span>
        </div>
      </header>

      {/* Navigation */}
      <nav className="app-nav">
        <button 
          className={activeView === 'cameras' ? 'nav-btn active' : 'nav-btn'}
          onClick={() => setActiveView('cameras')}
        >
          📹 Cameras
        </button>
        <button 
          className={activeView === 'science' ? 'nav-btn active' : 'nav-btn'}
          onClick={() => setActiveView('science')}
        >
          🔬 Science
        </button>
        <button 
          className={activeView === 'rado' ? 'nav-btn active' : 'nav-btn'}
          onClick={() => setActiveView('rado')}
        >
          🗺️ RADO
        </button>
        <button 
          className={activeView === 'dashboard' ? 'nav-btn active' : 'nav-btn'}
          onClick={() => setActiveView('dashboard')}
        >
          📊 Dashboard
        </button>
      </nav>

      {/* Main Content */}
      <main className="app-main">
        {/* Emergency Stop Button */}
        <button className="emergency-stop" onClick={handleEmergencyStop}>
          KILL
        </button>

        {/* Content Views */}
        {activeView === 'cameras' && (
          <div className="view-container">
            <CameraFeed title="Front Camera" feedId="1" />
            <CameraFeed title="Rear Camera" feedId="2" />
          </div>
        )}

        {activeView === 'science' && (
          <div className="view-container">
            <CameraFeed title="Science Camera" feedId="3" />
            <ScienceSensors scienceData={scienceData} />
          </div>
        )}

        {activeView === 'rado' && (
          <RadoView />
        )}

        {activeView === 'dashboard' && (
          <div className="view-container">
            <CameraFeed title="Main Camera" feedId="1" />
            <GPSDisplay gpsData={telemetryData.gps} />
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
