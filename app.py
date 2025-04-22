from flask import Flask, render_template, Response
import cv2
import torch

app = Flask(__name__)

# Load the YOLO model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Change to 'yolov8' if using YOLOv8

def generate_frames():
    cap = cv2.VideoCapture(0)  # Use 0 for webcam or replace with video file path
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Perform detection
        results = model(frame)
        frame = results.render()[0]

        # Encode the frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)