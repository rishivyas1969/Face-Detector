import cv2,os
from django.conf import settings
import requests

import numpy as np

face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'xml_file/frontface.xml'))
print(os.path.join(
			settings.BASE_DIR,'xml_file/frontface.xml'))

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		cv2.imwrite("send_to_flask.jpg", image)

		return image.tobytes()

class Feed(object):
	def get_saved_frame(self, name):
		file = {'image': open('send_to_flask.jpg', 'rb')}
		img_recieved = requests.post('http://127.0.0.1:5000/'+name, files=file)
		img_np = np.frombuffer(img_recieved.content, dtype=np.uint8)

		return img_np.tobytes()