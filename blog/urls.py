from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList, name='blog'),
    path('new/', views.CreateNewPost, name='CreateNewPost'),
]
