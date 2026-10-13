import json
from datetime import datetime

class RescueMarker:
    def __init__(self):
        self.markers = []

    def add(self, lat, lon, confidence, source="rgb"):
        self.markers.append({
            "lat": lat, "lon": lon,
            "confidence": confidence,
            "source": source,
            "timestamp": datetime.utcnow().isoformat()
        })

    def export_geojson(self, path="rescue_targets.geojson"):
        fc = {"type": "FeatureCollection", "features": [
            {"type": "Feature",
             "geometry": {"type": "Point", "coordinates": [m["lon"], m["lat"]]},
             "properties": m} for m in self.markers]}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(fc, f, ensure_ascii=False, indent=2)
