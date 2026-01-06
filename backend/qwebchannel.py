from PySide6.QtCore import QObject, Slot
import json

from backend.csv_manager import CSVLogger, WaypointLogCSV

'''
this class is the bridge between js map and python backend, every function in js ends up coming here which is redirected to csv manager
'''

class MapBackend(QObject):
    def __init__(self, csv_path: str, waypoint_log_csv: str):
        super().__init__()
        self.csv = CSVLogger(csv_path)
        self.wp_csv = WaypointLogCSV(waypoint_log_csv)


    @Slot(str, str)
    def receiveFromJS(self, eventType, jsonData):
        """Receive events from JavaScript"""
        print(f"Event: {eventType}")

        data = json.loads(jsonData)

        # ---------------- MARKERS ----------------
        if eventType == "newMarkerAdded":
            marker_id = self.csv.add_marker(
                lat=data["lat"],
                lon=data["lon"],
                label="waypoint"
            )
            print(f"  Marker added to CSV: ID {marker_id}")

        elif eventType == "markerRightClick":
            print(f"  Marker {data['id']} right-clicked at {data['lat']}, {data['lon']}")

        # ---------------- WAYPOINT LIST ----------------
        elif eventType == "waypointAdded":
            self.csv.add_to_waypoints(data["id"])
            print(f"  Added marker {data['id']} to waypoint list")

            wp_latlon = self.csv.get_waypoints_latlon()
            print(f"  Waypoints (lat/lon): {wp_latlon}")

                    # Also write to the new waypoint CSV
            marker = self.csv.get_marker(data["id"])
            if marker:
                self.wp_csv.add_waypoint(
                    lat=float(marker["lat"]),
                    lon=float(marker["lon"]),
                    yaw=float(marker["yaw"]) if marker["yaw"] else None
                )

        elif eventType == "waypointRemoved":
            marker = self.csv.get_marker(data["id"])

            if marker:
                self.wp_csv.remove_waypoint(
                    lat=float(marker["lat"]),
                    lon=float(marker["lon"])
                )

            self.csv.remove_from_waypoints(data["id"])
            print(f"  Removed marker {data['id']} from waypoint list")

        elif eventType == "waypointsReset":
            self.csv.reset_waypoints()
            self.wp_csv.reset()
            print("  All waypoints reset")

        # ---------------- CONNECTIONS ----------------
        elif eventType == "markersConnected":
            self.csv.add_connection(data["from"], data["to"])
            print(f"  Connected {data['from']} <-> {data['to']}")

        elif eventType == "markerDisconnected":
            self.csv.remove_connection(data["markerId"])
            print(f"  Removed all connections for marker {data['markerId']}")

        elif eventType == "allConnectionsRemoved":
            self.csv.reset_connections()
            print("  All connections removed")

        # ---------------- MAP EVENTS ----------------
        elif eventType == "mapRightClick":
            print(f"  Map right-clicked at {data['lat']}, {data['lon']}")

        elif eventType == "markerSelected":
            print(f"  Marker selected for connection: {data['id']}")

    def get_waypoints_for_map(self):
        return self.csv.get_waypoints_for_map()

    @Slot()
    def onPageReady(self):
        """Called when the HTML page is fully loaded"""
        print("Map page is ready!")

        markers = self.csv.get_all_markers()
        print(f"Loaded {len(markers)} markers from CSV")


