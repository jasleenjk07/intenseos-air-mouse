import cv2

from core.vision.fps_counter import FPSCounter
from core.vision.hand_detector import HandDetector

from core.tracking.cursor_mapper import CursorMapper
from core.actions.mouse_controller import MouseController

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
        self.hand_detector = HandDetector()
        self.cursor_mapper = CursorMapper()
        self.mouse_controller = MouseController()

    def start_stream(self):
        while True:
            success, frame = self.cap.read()

            if not success:
                print("Failed to access webcam")
                break

            frame = cv2.flip(frame, 1)

            frame = self.hand_detector.detect_hands(frame)

            landmarks = self.hand_detector.get_landmark_positions(frame)

            if landmarks:
                index_finger_tip = landmarks[8]

                _, x, y = index_finger_tip

                cv2.rectangle(
                    frame,
                    (100, 100),
                    (self.width - 100, self.height - 100),
                    (0, 255, 0),
                    2
                )

                cv2.circle(frame, (x, y), 15, (255, 0, 255), cv2.FILLED)

                cursor_x, cursor_y = self.cursor_mapper.map_position(x, y, self.width, self.height)

                if 100 < x < self.width - 100 and 100 < y < self.height - 100:
                    self.mouse_controller.move_cursor(cursor_x, cursor_y)

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

            cv2.imshow("IntentOS Hand Tracking", frame)

            key = cv2.waitKey(1)

            if key == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()