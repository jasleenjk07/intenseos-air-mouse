import pyautogui


class CursorMapper:
    def __init__(
        self,
        smoothing=7,
        frame_reduction=250
    ):

        self.screen_width, self.screen_height = pyautogui.size()

        self.previous_x = 0
        self.previous_y = 0

        self.current_x = 0
        self.current_y = 0

        self.smoothing = smoothing
        self.frame_reduction = frame_reduction

    def map_position(
        self,
        finger_x,
        finger_y,
        frame_width,
        frame_height
    ):

        usable_width = frame_width - (2 * self.frame_reduction)
        usable_height = frame_height - (2 * self.frame_reduction)

        finger_x = max(
            self.frame_reduction,
            min(finger_x, frame_width - self.frame_reduction)
        )

        finger_y = max(
            self.frame_reduction,
            min(finger_y, frame_height - self.frame_reduction)
        )

        normalized_x = (
            finger_x - self.frame_reduction
        ) / usable_width

        normalized_y = (
            finger_y - self.frame_reduction
        ) / usable_height

        screen_x = normalized_x * self.screen_width
        screen_y = normalized_y * self.screen_height

        self.current_x = self.previous_x + (
            screen_x - self.previous_x
        ) / self.smoothing

        self.current_y = self.previous_y + (
            screen_y - self.previous_y
        ) / self.smoothing

        self.previous_x = self.current_x
        self.previous_y = self.current_y

        return int(self.current_x), int(self.current_y)