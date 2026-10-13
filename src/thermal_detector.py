import cv2
import numpy as np

class ThermalDetector:
    """Детекция горячих объектов (люди) по температуре."""
    def __init__(self, min_temp_c=28, max_temp_c=42):
        self.t_min = min_temp_c
        self.t_max = max_temp_c

    def detect(self, thermal_frame, scale_to_celsius=None):
        if scale_to_celsius:
            temp = thermal_frame.astype(np.float32) * scale_to_celsius
        else:
            temp = thermal_frame.astype(np.float32)
        mask = ((temp >= self.t_min) & (temp <= self.t_max)).astype(np.uint8) * 255
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 30]
