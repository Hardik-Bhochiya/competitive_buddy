from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor_page, name="mentor"),
    path('chat/', views.mentor_chat, name="mentor_chat"),
]