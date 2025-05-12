from picamera2 import Picamera2
import cv2
import numpy as np
import tensorflow as tf
import time

# pre-train model
"""
MODEL_PATH = "vegetable_model.tflite"
LABELS = [...]

# Initialize TFLite interpreter
interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape'][1:3]  # (height, width)
"""

def run_cam():

    # Initialize camera
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (640, 480)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.configure("preview")
    picam2.start()
    time.sleep(2)  # allow camera to warm up

    def preprocess(image):
        image = cv2.resize(image, tuple(input_shape))
        image = image.astype(np.float32) / 255.0
        return np.expand_dims(image, axis=0)

    try:
        while True:
            frame = picam2.capture_array()
            input_data = preprocess(frame)

            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()

            output_data = interpreter.get_tensor(output_details[0]['index'])[0]
            prediction = LABELS[np.argmax(output_data)]
            confidence = np.max(output_data)

            # Display result
            cv2.putText(frame, f"{prediction} ({confidence:.2f})", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Vegetable Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        picam2.stop()
        cv2.destroyAllWindows()