import math

class GestureDetector:
    def __init__(self, click_threshold = 35):
        self.click_threshold = click_threshold

    def calculate_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2

        distance = math.hypot(x2 - x1, y2 - y1)

        return distance

    def detect_click(self, landmarks):
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]

        _, thumb_x, thumb_y = thumb_tip
        _, index_x, index_y = index_tip

        distance = self.calculate_distance((thumb_x, thumb_y), (index_x, index_y))

        is_click = distance < self.click_threshold

        return is_click, distance