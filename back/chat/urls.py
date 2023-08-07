from django.urls import path, include
from . import views


urlpatterns = [
    path('classification/', views.ClassificationView.as_view(), name='Classification-chat'),
    path('lawgpt/', views.LawgptView.as_view(), name='Lawgpt-chat'),
]