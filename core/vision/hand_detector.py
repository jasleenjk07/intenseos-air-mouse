import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, static_mode = False, max_hands = 1, detection_confidence = 0.7, tracking_confidence = 0.7):
        self.static_mode = static_mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode = self.static_mode,
            max_num_hands = self.max_hands,
            min_detection_confidence = self.detection_confidence,
            min_tracking_confidence = self.tracking_confidence
        )

    def detect_hands(self, frame, draw = True):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.hands = self.hands.process(rgb_frame)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )

        return frame

    def get_landmark_positions(self, frame, hand_index = 0):
        landmark_list = []

        if self.results.multi_hand_landmarks:
            selected_hand = self.results.mutli_hand_landmarks[hand_index]

            height, width, _ = frame.shape

            for landmark_id, landmark in enumerate(selected_hand.landmark):
                x_position = int(landmark.x * width)
                y_position = int(landmark.y * height)

                landmark_list.append(
                    (landmark_id, x_position, y_position)
                )

        return landmark_list