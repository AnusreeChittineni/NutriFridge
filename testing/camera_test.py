from picamera2 import Picamera2
import cv2
import time

# Initialize the camera
picam2 = Picamera2()

# Set camera configuration
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")

# Start camera
picam2.start()
time.sleep(2)  # Give it time to warm up

# Capture and display frames
try:
    while True:
        frame = picam2.capture_array()
        cv2.imshow("Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

finally:
    picam2.stop()
    cv2.destroyAllWindows()
