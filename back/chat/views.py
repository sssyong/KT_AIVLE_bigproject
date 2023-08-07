from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import ClassificationChat, LawgptChat
from .serializers import ClassificationSerializer, LawgptSerializer
                        
from django.http import HttpResponse
import requests
# Create your views here.

class ClassificationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user:
            other_app_url = 'http://127.0.0.1:8000/accounts/authVerify/'
            request_data = {"token" : request.auth}
            response = requests.post(other_app_url, data=request_data)
            response_json = response.json()
            
            classification = ClassificationChat.objects.filter(user_id = response_json['user_id'])
            
            result = []
            for data in classification:
                result_data = {}
                result_data['user'] = data.user_id
                result_data['message'] = data.message
                result_data['answer'] = data.answer
                result_data['category'] = data.category_id
                
                result.append(result_data)
                
            response_data = {"result" : result}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = ClassificationSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            return Response(status=status.HTTP_201_CREATED)
        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LawgptView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        
        if request.user:
            other_app_url = 'http://127.0.0.1:8000/accounts/authVerify/'
            request_data = {"token" : request.auth}
            response = requests.post(other_app_url, data=request_data)
            response_json = response.json()
            
            lawgpt = LawgptChat.objects.filter(user_id = response_json['user_id'])
            
            result = []
            for data in lawgpt:
                result_data = {}
                result_data['user'] = data.user_id
                result_data['message'] = data.message
                result_data['answer'] = data.answer
                
                result.append(result_data)
                
            response_data = {"result" : result}
            return Response(response_data, status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = LawgptSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)