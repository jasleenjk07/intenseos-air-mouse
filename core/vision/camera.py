import cv2

from core.vision.fps_counter import FPSCounter

class CameraStream:
    def __init__(self, camera_index=0, width=1280, height=720):
        self.camera_index = camera_index
        self.width = width
        self.height = height

        self.cap = cv2.VideoCapture(
            self.camera_index,
            cv2.CAP_AVFOUNDATION
        )

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        self.fps_counter = FPSCounter()

    def start_stream(self):
        while True:
            success, frame = self.cap.read()

            if not success:
                print("Failed to access webcam")
                break

            frame = cv2.flip(frame, 1)

            fps = self.fps_counter.calculate_fps()

            cv2.putText(
                frame,
                f"FPS: {fps}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow("IntentOS Camera Feed", frame)

            key = cv2.waitKey(1)

            if key == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()