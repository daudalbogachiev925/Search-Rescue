def iou(a, b):
    xa, ya = max(a[0], b[0]), max(a[1], b[1])
    xb, yb = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, xb - xa) * max(0, yb - ya)
    aa = (a[2]-a[0]) * (a[3]-a[1])
    ab = (b[2]-b[0]) * (b[3]-b[1])
    return inter / (aa + ab - inter + 1e-6)

def fuse(rgb_boxes, thermal_boxes, iou_threshold=0.2):
    """Объединяет детекции: подтверждённые = RGB + Thermal."""
    confirmed = []
    for rb in rgb_boxes:
        thermal_match = any(iou(rb, tb) > iou_threshold for tb in thermal_boxes)
        confirmed.append({"bbox": rb, "thermal": thermal_match,
                          "confidence": 1.0 if thermal_match else 0.6})
    return confirmed
