from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from stream.camera import VideoCamera, Feed

# Create your views here.

def index(request):

    return render(request, 'stream/index.html')

def gen(camera):

    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):

    return StreamingHttpResponse(gen(VideoCamera()),
                                content_type='multipart/x-mixed-replace; boundary=frame')

def genFromSaved(camera, name):

    while True:
        frame = camera.get_saved_frame(name)
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def saved_video_feed(request, name):

    return StreamingHttpResponse(genFromSaved(Feed(), name),
                                content_type='multipart/x-mixed-replace; boundary=frame')    