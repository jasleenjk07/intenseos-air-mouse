import pyautogui

class MouseController:
    def __init__(self):
        pyautogui.FAILSAFE = False

    def move_cursor(self, x, y):
        pyautogui.moveTo(x, y, _pause = False)

    def left_click(self):
        pyautogui.click()