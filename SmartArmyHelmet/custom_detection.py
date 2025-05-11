# custom_detection.py
import cv2
from yolov5 import detect  # Importing detect from YOLOv5

# Load the YOLOv5 model
model = detect.load_model('yolov5s.pt')

# Capture video from laptop camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection on the frame
    results = model(frame)
    results.show()  # Display detected objects

    # Save output image or video
    results.save()  # Saves output in specified folder
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

