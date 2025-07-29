# YOLOv8 Weed Detection AI

This project builds an AI-powered weed detection system using Python, OpenCV, YOLOv8, and other libraries.  It detects weeds in garden images and videos, labeling them with bounding boxes.

### 📦 Dataset Overview
- weed_dataset - contains '.jpg' images with weeds, each labeled with bounding boxes {'.txt' in YOLO format}
- not_weed_dataset - contains '.jpg' images with no weeds.  Each image has an empty '.txt' label file.        

All labels were created in Pascal VOC .xml format and converted to YOLO .txt format.

## 📁 Folder Structure

- project/
- ├── weed_dataset/ # Images with weed and XML annotations 
- ├── not_weed_dataset/ # Images without weed (blank annotations)
- ├── dataset/ # Output folder after running org.py (YOLOv8 format)
- │ ├── images/train/
- │ ├── images/val/
- │ ├── labels/train/
- │ └── labels/val/
- ├── org.py # Organizes data into YOLOv8 format
- ├── detect_weed.py # Detects weeds in a video
- ├── README.md # You're here!
- └── yolov8n.yaml # Custom YAML for training config (if needed)



## 🔧 Features

### 'org.py' - Dataset organizer:
- Collects all `.jpg` and corresponding `.txt` files from both datasets.
- Splits the data into:
  - **80% training**
  - **20% validation**
- Outputs a YOLOv8-compliant structure inside `dataset/`.

### `data.yaml` — Training Configuration
- Specifies:
  - Paths to training and validation folders
  - It specifies that the training images are in images/train.
  - It also specifies that the validation images are in images/val.
  - Class names (only one: `"weed"`)


## 🎥 Inference on Videos
### `detect_weed.py`:
- Loads the trained YOLOv8 model (default: `runs/detect/train/weights/best.pt`)
- Opens the input video file
- Processes the video **frame by frame**
- Draws bounding boxes for each frame
- Saves the output video as `output.avi`
- Optionally displays the live output window



## 🧠 Training the YOLOv8 Model
## ONLY RUN IF DETECTION VIDEO IS NOT WORKING AS INTENDED##
yolo detect train model=yolov8n.pt data=dataset/data.yaml epochs=50 imgsz=640




##🚀 How to Run the Program
------------------------------------------------------------------------------------------------------
## 🧪 Running Detection on a Video
- Upload your video file (e.g. .mov, .mp4) to the weed_videos folder.
- If your video file has a different extension (e.g. .mp4 instead of .mov), update the command accordingly.



python detect_weed.py weed_videos/path_to_input_video.mov



