class SearchMission:
    def __init__(self, area_km2, drone_speed_mps=15, sensor_width_m=50):
        self.area = area_km2
        self.speed = drone_speed_mps
        self.swath = sensor_width_m

    def lawnmower_path(self, width_m, height_m):
        path = []
        y = 0
        step = self.swath
        direction = 1
        while y <= height_m:
            if direction > 0:
                path.append((0, y)); path.append((width_m, y))
            else:
                path.append((width_m, y)); path.append((0, y))
            y += step
            direction *= -1
        return path

    def estimate_time_min(self, width_m, height_m):
        path = self.lawnmower_path(width_m, height_m)
        total_dist = 0
        for i in range(1, len(path)):
            total_dist += ((path[i][0]-path[i-1][0])**2 +
                           (path[i][1]-path[i-1][1])**2) ** 0.5
        return total_dist / self.speed / 60
