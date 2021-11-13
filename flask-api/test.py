import requests
import cv2
import numpy as np

cam = cv2.VideoCapture(0)
_ , frame = cam.read()
cv2.imwrite('test2.jpg', frame)

url = 'http://127.0.0.1:5000/blue'
file = {'image': open('test2.jpg', 'rb')}

content = requests.post(url, files=file)
print(type(content.content))
img_np = np.frombuffer(content.content, dtype=np.uint8)
img = cv2.imdecode(img_np, flags=1)
cv2.imwrite("imgFromAPI.jpg",img)
# cv2.imwrite('result.jpg', content.content)
print(content)