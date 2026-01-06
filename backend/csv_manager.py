import csv
from typing import List, Dict, Optional
import os

class CSVLogger:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.fieldnames = ["id", "lat", "lon", "label", "connections", "in_waypoints", "yaw"]

        if not os.path.exists(self.csv_path):
            self._write([])

    def _read(self):
        with open(self.csv_path, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        return rows

    def _write(self, rows):
        tmp_path = self.csv_path + ".tmp"

        with open(tmp_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        os.replace(tmp_path, self.csv_path)  # atomic on Linux

    def add_marker(self, lat: float, lon: float, label: str = "waypoint", yaw = None) -> int:
        """Add a new marker (not automatically a waypoint)"""
        rows = self._read()
        new_id = max([int(r["id"]) for r in rows], default=-1) + 1

        row = {
            "id": new_id,
            "lat": lat,
            "lon": lon,
            "label": label,
            "connections": "",
            "in_waypoints": "False",
            "yaw": yaw if yaw is not None else "0.0"
        }
        rows.append(row)
        self._write(rows)
        return new_id

    def add_to_waypoints(self, marker_id: int):
        rows = self._read()
        for row in rows:
            if int(row["id"]) == marker_id:
                row["in_waypoints"] = "True"
                row["label"] = "waypoint_selected"
        self._write(rows)

    def remove_from_waypoints(self, marker_id: int):
        rows = self._read()
        for row in rows:
            if int(row["id"]) == marker_id:
                row["in_waypoints"] = "False"
                row["label"] = "waypoint"
        self._write(rows)

    def add_connection(self, from_id: int, to_id: int):
        rows = self._read()
        updated = False
        for row in rows:
            if int(row["id"]) == from_id:
                connections = [c for c in row["connections"].split(",") if c.strip()]
                if str(to_id) not in connections:
                    connections.append(str(to_id))
                    row["connections"] = ",".join(connections)
                    updated = True
            elif int(row["id"]) == to_id:
                connections = [c for c in row["connections"].split(",") if c.strip()]
                if str(from_id) not in connections:
                    connections.append(str(from_id))
                    row["connections"] = ",".join(connections)
                    updated = True
        if updated:
            self._write(rows)

    def remove_connection(self, marker_id: int):
        """Remove all connections involving this marker"""
        rows = self._read()
        updated = False
        for row in rows:
            connections = [c for c in row["connections"].split(",") if c.strip()]
            if str(marker_id) in connections:
                connections.remove(str(marker_id))
                row["connections"] = ",".join(connections)
                updated = True
        # Also clear its own connections
        for row in rows:
            if int(row["id"]) == marker_id:
                row["connections"] = ""
                updated = True
        if updated:
            self._write(rows)

    def reset_waypoints(self):
        rows = self._read()
        for row in rows:
            row["in_waypoints"] = "False"
            if row["label"] == "waypoint_selected":
                row["label"] = "waypoint"
        self._write(rows)

    def reset_connections(self):
        rows = self._read()
        for row in rows:
            row["connections"] = ""
        self._write(rows)


    def get_all_markers(self) -> List[Dict]:
        rows = self._read()
        # Convert proper types
        markers = []
        for r in rows:
            markers.append({
                "id": int(r["id"]),
                "lat": float(r["lat"]),
                "lon": float(r["lon"]),
                "label": r["label"],
                "connections": [int(c) for c in r["connections"].split(",") if c.strip()],
                "in_waypoints": r["in_waypoints"] == "True",
                "yaw": float(r["yaw"]) if r["yaw"] else None
            })
        return markers

    def get_marker(self, marker_id: int) -> Optional[Dict]:
        rows = self._read()
        for r in rows:
            if int(r["id"]) == marker_id:
                return r
        return None
    
    # ===============================
    # GET WAYPOINT COORDINATES
    # ===============================
    def get_waypoints_latlon(self) -> List[Dict[str, float]]:
        """
        Returns list of dicts containing lat/lon of markers
        that are currently part of the waypoints list.
        Example:
        [
            {"lat": 12.9916, "lon": 80.2346},
            {"lat": 12.9925, "lon": 80.2340},
            ...
        ]
        """
        rows = self._read()
        waypoints = []
        for r in rows:
            if r["in_waypoints"] == "True":
                waypoints.append({
                    "lat": float(r["lat"]),
                    "lon": float(r["lon"])
                })
        return waypoints
    
    def get_waypoints_for_map(self):
        """
        Returns list of dicts safe to send directly to JS.
        All values are converted to correct types.
        """
        rows = self._read()
        result = []

        for row in rows:
            result.append({
                "id": int(row["id"]),
                "lat": float(row["lat"]),
                "lon": float(row["lon"]),
                "label": row.get("label", ""),
                "connections": row.get("connections", ""),
                "in_waypoints": row.get("in_waypoints", ""),
                "yaw": row.get("yaw", "")
            })

        return result


class WaypointLogCSV:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.fieldnames = ["lat", "lon", "yaw"]

        if not os.path.exists(self.csv_path):
            with open(self.csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()

    def _read(self):
        with open(self.csv_path, "r", newline="") as f:
            return list(csv.DictReader(f))

    def _write(self, rows):
        tmp = self.csv_path + ".tmp"
        with open(tmp, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(tmp, self.csv_path)  # atomic


    def add_waypoint(self, lat: float, lon: float, yaw: float = None, tol=1e-7):
        rows = self._read()

        # prevent duplicates
        for r in rows:
            if abs(float(r["lat"]) - lat) < tol and abs(float(r["lon"]) - lon) < tol:
                return

        rows.append({
            "lat": lat,
            "lon": lon,
            "yaw": yaw if yaw is not None else ""
        })
        self._write(rows)

    def remove_waypoint(self, lat: float, lon: float, tol=1e-7):
        rows = self._read()
        rows = [
            r for r in rows
            if not (
                abs(float(r["lat"]) - lat) < tol and
                abs(float(r["lon"]) - lon) < tol
            )
        ]
        self._write(rows)

    def reset(self):
        self._write([])


