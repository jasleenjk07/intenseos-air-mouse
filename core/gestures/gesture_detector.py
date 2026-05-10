import math
import time

class GestureDetector:
    def __init__(self, click_threshold = 35, click_cooldown = 0.4, hold_threshold = 0.8):
        self.click_threshold = click_threshold
        self.click_cooldown = click_cooldown
        self.hold_threshold = hold_threshold
        self.last_click_time = 0
        self.pinch_start_time = None

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

        is_pinching = distance < self.click_threshold

        current_time = time.time()

        should_click = False
        is_holding = False

        if is_pinching:
            if self.pinch_start_time is None:
                self.pinch_start_time = current_time

                pinch_duration = (current_time - self.pinch_start_time)

                if pinch_duration >= self.hold_threshold:
                    is_holding = True

                if (current_time - self.last_click_time >= self.click_cooldown):
                    should_click = True
                    self.last_click_time = current_time
        
        else:
            self.pinch_start_time = None

        return {
            "distance": distance,
            "is_pinching": is_pinching,
            "should_click": should_click,
            "is_holding": is_holding
        }