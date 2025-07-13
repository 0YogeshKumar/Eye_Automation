import argparse
import cv2
import dlib
import imutils
import time
from imutils.video import VideoStream
from imutils import face_utils
from scipy.spatial import distance as dist
import winsound
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

class BlinkDetector:
    def __init__(self, video_stream, facial_landmark_predictor):
        """
        Initialize the blink detector with a video stream and facial landmark predictor.
        """
        self.video_stream = video_stream
        self.facial_landmark_predictor = facial_landmark_predictor
        self.eye_aspect_ratio_threshold = 0.25
        self.consecutive_frames_threshold = 3
        self.COUNTER = 0
        self.TOTAL = 0

    def calculate_eye_aspect_ratio(self, eye):
        """
        Calculate the eye aspect ratio for a given eye.
        """
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def detect_blinks(self):
        """
        Detect blinks in the video stream.
        """
        while True:
            frame = self.video_stream.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rects = detector(gray, 0)

            for rect in rects:
                shape = self.facial_landmark_predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
                left_eye = shape[lStart:lEnd]
                right_eye = shape[rStart:rEnd]
                left_ear = self.calculate_eye_aspect_ratio(left_eye)
                right_ear = self.calculate_eye_aspect_ratio(right_eye)
                ear = (left_ear + right_ear) / 2.0

                if ear < self.eye_aspect_ratio_threshold:
                    self.COUNTER += 1
                else:
                    if self.COUNTER >= self.consecutive_frames_threshold:
                        self.TOTAL += 1
                        if self.TOTAL == 8:
                            self.TOTAL = 0
                            engine.say("Blink detected")
                            engine.runAndWait()
                            winsound.Beep(2500, 1000)
                    self.COUNTER = 0

                cv2.putText(frame, "Blinks: {}".format(self.TOTAL), (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

def main():
    """
    Main function to start the blink detection.
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--shape-predictor", required=True,
                    help="path to facial landmark predictor")
    ap.add_argument("-v", "--video", type=str, default="",
                    help="path to input video file")
    args = vars(ap.parse_args())

    global detector, predictor, lStart, lEnd, rStart, rEnd
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(args["shape_predictor"])
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    vs = VideoStream(src=0).start()
    time.sleep(1.0)

    blink_detector = BlinkDetector(vs, predictor)
    blink_detector.detect_blinks()

    cv2.destroyAllWindows()
    vs.stop()

if __name__ == "__main__":
    main()