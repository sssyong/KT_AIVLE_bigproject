# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.http import JsonResponse
# from .serializer import MyTokenObtainPairSerializer, RegisterSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework import generics
# from django.contrib.auth.models import User
# from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserIdPostSerializer
from main import local_settings
import requests
import jwt

class UserIdRespone(APIView):
    
     def post(self, request):
        serializer = UserIdPostSerializer(data = request.data)
        
        if serializer.is_valid():
            verify_token_url = "http://127.0.0.1:8000/accounts/dj-rest-auth/token/verify/"

            # 확인할 토큰
            token_to_verify = serializer.data['token']

            # 토큰 확인 요청 보내기
            response = requests.post(verify_token_url, json={"token": token_to_verify})
            
            # 토큰 확인 응답 처리
            if response.status_code == 200:
                # 토큰이 유효한 경우 디코드하여 사용자 아이디 가져오기
                decoded_token = jwt.decode(token_to_verify, local_settings.SECRET_KEY, algorithms=["HS256"])
                
                user_id = decoded_token.get("user_id")
                response_data = {"user_id": user_id}
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                # 토큰이 유효하지 않은 경우 처리
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
# from .serializer import RegistrationSerializer, LoginSerializer
# from .renderers import UserJSONRenderer

# class RegistrationAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = RegistrationSerializer
#     renderer_classes = (UserJSONRenderer,)
    
#     def post(self, request):
#         user = request.data
        
#         serializer = self.serializer_class(data=user)
#         if serializer.is_valid(raise_exception=True):
#             serializer.create()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = LoginSerializer
    
#     # 1.
#     def post(self, request):
#         # 2.
#         user = request.data
        
#         # 3.
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
        
#         # 4.
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# # Create your views here.

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer


# @api_view(['GET', 'POST'])
# def getRoutes(request):
#     routes = [
#         '/api/token/',
#         '/api/register/',
#         '/api/token/refresh/'
#     ]
#     return Response(routes)