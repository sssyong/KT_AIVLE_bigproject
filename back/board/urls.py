# Board/views.py
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'Board'
urlpatterns = [
    path("", views.ListBoard.as_view(), name='list-board'),
    path("create/", views.CreateBoard.as_view(), name='create-board'),
    path('id/<int:pk>/', views.DetailBoard.as_view(), name='detail-board'),
    path("user/", views.ListUserBoard.as_view(), name='list-user-board'),
]