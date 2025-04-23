# Real-Time Grocery Item Detection
This project demonstrates a real-time object detection web application built using Flask and the YOLO (You Only Look Once) deep learning model. The system captures video from a webcam (or a video file), performs object detection using the YOLO model, and streams the results on a webpage. The application is designed to detect grocery items or any other objects that the YOLO model has been trained to identify.

--- 

#TEAM MEMBERS
- YASHAN OSWAL (KU2407U448/202407020426)
- OMI RATHOD (KU2407U429/202407020408)
- KANISHK LADDHA (KU2407U413/202407020392)
 ---
 
##Features
- Real-Time Object Detection: The application detects objects in video frames in real-time, annotating the detected items with labels and bounding boxes.
- Web Interface: The application provides a simple webpage interface that displays the real-time video feed from the webcam, including object detection annotations.
- Multiple Object Detection: You can customize the model to detect various objects based on the pre-trained YOLO model, such as groceries, animals, people, etc.
- Scalability: The application can be easily adapted to work with different video sources, such as webcam, video files, or even IP cameras.

---

## Tools and Libraries Used
- Flask: A lightweight WSGI web application framework for Python. It is used to serve the web application and handle HTTP requests, including the video feed.
- OpenCV: A powerful open-source computer vision library that is used for handling image and video processing tasks, such as reading frames from the webcam or video files, and encoding them to be streamed.
- PyTorch: An open-source machine learning library used for running the YOLO model. PyTorch provides the necessary tools for deep learning and inference, enabling real-time object detection.
- YOLOv5: A state-of-the-art object detection model designed by Ultralytics, which is used in this project for real-time object detection. YOLOv5 is capable of detecting multiple objects in an image or video feed with high accuracy.
- HTML/CSS: Standard web technologies used to create the user interface of the application, displaying the video feed on a webpage.

---

##How It Works
- Flask Web Application:
The main Flask application serves the HTML page (index.html), which contains an image element that continuously requests video frames from the backend.
The video frames are served by Flask through the /video_feed route, which streams JPEG images to the client.

- Video Capture:
The application captures video frames using OpenCV (cv2.VideoCapture(0)), which accesses the webcam (or any video source specified by the user).

- Object Detection with YOLO:
Each captured frame is passed to the YOLO model (YOLOv5 in this case) for object detection. The model processes the frame and returns the bounding boxes and class labels of the detected objects.
The detected objects are then rendered onto the frame with bounding boxes and class labels by the render() function of the YOLO model.

- Frame Encoding:
After processing the frame, it is encoded in JPEG format using OpenCV (cv2.imencode()) to reduce the size for efficient transmission over the web.

- Real-Time Streaming:
The Flask server continuously streams the encoded frames to the webpage using multipart streaming, where each frame is sent as part of a continuous HTTP response. This allows the video feed to update in real-time on the client’s browser.

- Frontend (Webpage):
The webpage displays the video stream using an HTML <img> element that points to the /video_feed route.
The webpage auto-updates the displayed image as new frames are streamed from the server.

---

## Model Versions:
- YOLOv5: The yolov5s, yolov5m, yolov5l, and yolov5x are different versions of YOLOv5, with yolov5s being the smallest and fastest, and yolov5x being the largest with the best accuracy but slower speed.
- YOLOv8: A similar approach applies to YOLOv8 models where the small version (yolov8n) is faster and the larger versions (yolov8l, yolov8x) have better accuracy but slower inference.
