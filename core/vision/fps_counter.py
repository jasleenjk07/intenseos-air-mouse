import time

class FPSCounter:
    def __init__(self):
        self.previous_time = 0 #Stores the time of the previous frame.
        self.current_time = 0 #Stores the time of the current frame.


    def calculate_fps(self):
        self.current_time = time.time() #returns the current time in seconds

        fps = 0

        if self.current_time != self.previous_time:
            fps = 1 / (self.current_time - self.previous_time)

        self.previous_time = self.current_time

        return int(fps)