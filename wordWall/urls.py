from django.urls import path
from . import views

urlpatterns = [
    path('wordWall', views.wordWall_Index, name='wordWallHome'),
]