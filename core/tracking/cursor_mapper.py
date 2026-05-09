import pyautogui


class CursorMapper:
    def __init__(self, smoothing=7):

        self.screen_width, self.screen_height = pyautogui.size()

        self.previous_x = 0
        self.previous_y = 0

        self.current_x = 0
        self.current_y = 0

        self.smoothing = smoothing

    def map_position(
        self,
        finger_x,
        finger_y,
        frame_width,
        frame_height
    ):

        screen_x = (finger_x / frame_width) * self.screen_width
        screen_y = (finger_y / frame_height) * self.screen_height

        self.current_x = self.previous_x + (
            screen_x - self.previous_x
        ) / self.smoothing

        self.current_y = self.previous_y + (
            screen_y - self.previous_y
        ) / self.smoothing

        self.previous_x = self.current_x
        self.previous_y = self.current_y

        return int(self.current_x), int(self.current_y)