from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Board
from .serializers import BoardSerializer, BoardUserSerializer

# Create your views here.

class CreateBoard(generics.CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    
class ListBoard(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardUserSerializer
    pagination_class = CustomPagination
    
class DetailBoard(generics.RetrieveUpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardUserSerializer
    
class ListUserBoard(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Board.objects.filter(user=user, deleted_at=None)
        else:
            return Board.objects.none()