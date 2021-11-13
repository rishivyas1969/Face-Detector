from django.urls import path, include
from django.urls import path, include
from stream import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('saved_video_feed/<str:name>', views.saved_video_feed, name='saved_video_feed')
]

