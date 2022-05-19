import os
from aiymakerkit import vision
from flask import Flask
from flask import render_template
from flask import Response
import cv2
"""
Run this app on a Raspberry Pi to start a live video stream with face detection:

    python3 app.py

Then, from another computer on the same network, open a browser and enter
the Raspberry Pi IP address (run `hostname -I` on the Raspberry Pi to find it).
For example: http://192.168.86.42
"""

FACE_DETECTION_MODEL = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'ssd_mobilenet_v2_face_quant_postprocess_edgetpu.tflite')

app = Flask(__name__)
detector = vision.Detector(FACE_DETECTION_MODEL)

def get_frames():
    # Get camera frames and run inference with aiymakerkit
    for frame in vision.get_frames(display=False):
        faces = detector.get_objects(frame, threshold=0.1)
        vision.draw_objects(frame, faces)

        # Convert to JPG bytes so we can render images in a web page
        _, img_buffer = cv2.imencode('.jpg', frame)
        img_bytes = img_buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)