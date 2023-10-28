from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('health_test/', views.health_test, name='health_test'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('video_conference/', views.video_conference, name='video_conference'),
]