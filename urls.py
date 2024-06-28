from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chat'),
    path('chatbot_view', views.chatbot_view, name='chatbot_view'),
    path('authentication-login/', views.authentication_login ,name="authentication-login"),
    path('authentication-register/', views.authentication_register ,name="authentication-register"),
    path('authentication-signout/', views.authentication_signout ,name="authentication-signout"),
    path('fetch_response_from_views.py', views.chatbot_view, name='fetch_response'),
    path('send-message/', views.chatbot_view, name='send_message'),
]
