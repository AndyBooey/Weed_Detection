import sys
import cv2
from ultralytics import YOLO

# Check for the video path argument
if len(sys.argv) < 2:
    print("⚠️ Failed to detect video.  Exiting...")
    sys.exit()
 
video_path = sys.argv[1]

# Optional: Let user input the model path
model = YOLO("runs/detect/train7/weights/best.pt")  

# Try to open the video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"❌ Error: Cannot open the video: {video_path}")
    sys.exit()

print(f"Running video detection on: '{video_path}'")

# Get frame size for output video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("The end of the video has been reached.")
        break

    # 🔍 Run detection
    results = model(frame)
    frame = results[0].plot()

    # 🖼️ Show detection
    cv2.imshow("Weed Detector", frame)

    # 💾 Save output
    out.write(frame)

    # Print number of detected weeds (objects)
    print(f"Weeds detected: {len(results[0].boxes)}")

    # 🚪 Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting the video...")
        break

# 🔚 Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()
