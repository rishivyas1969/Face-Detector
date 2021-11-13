from sys import flags
from flask import Flask, request, send_file
import numpy as np
import cv2
from werkzeug import datastructures

face_detection_videocam = cv2.CascadeClassifier('frontalface.xml')

app = Flask(__name__)

def performOperation(image, color):
    print(color)
    if color in 'blue':
        rgb_color = (255, 0, 0)
    elif color in 'green':
        rgb_color = (0,255,0)
    else: 
        rgb_color = (0, 0, 255)
    image =np.frombuffer(image, np.uint8)
    image_arr = cv2.imdecode(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
    faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces_detected:
        cv2.rectangle(image_arr, pt1=(x, y), pt2=(x + w, y + h), color=rgb_color, thickness=2)
    frame_flip = cv2.flip(image_arr,1)
    ret, jpeg = cv2.imencode('.jpg', frame_flip)
    cv2.imwrite(color+"result.jpg", frame_flip)
    return jpeg.tobytes()

@app.route('/blue', methods=['POST', 'GET'])
def indexforblue():
    if request.method == 'POST':
        image = request.files['image'].read()
        image = performOperation(image, "blue")
        return send_file("blueresult.jpg", mimetype="image/jpeg", as_attachment=True, attachment_filename='result.jpg')

@app.route('/green', methods=['POST', 'GET'])
def indexforgreen():
    if request.method == 'POST':
        image = request.files['image'].read()
        image = performOperation(image, "green")
        return send_file("greenresult.jpg", mimetype="image/jpeg", as_attachment=True, attachment_filename='result.jpg')

@app.route('/red', methods=['POST', 'GET'])
def indexforred():
    if request.method == 'POST':
        image = request.files['image'].read()
        image = performOperation(image, "red")
        return send_file("redresult.jpg", mimetype="image/jpeg", as_attachment=True, attachment_filename='result.jpg')

if __name__ == "__main__":
    app.run(debug=True)