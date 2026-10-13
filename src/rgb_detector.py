from ultralytics import YOLO

class RGBPersonDetector:
    def __init__(self, model_path="yolov8n.pt", conf=0.3):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        res = self.model.predict(frame, conf=self.conf, classes=[0], verbose=False)[0]
        return [b.xyxy[0].tolist() for b in res.boxes]
