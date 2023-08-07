# import os
# import uuid

from django.contrib.auth.models import User, AbstractUser
from django.db import models
# from rest_framework import serializers

import jwt
from datetime import datetime, timedelta
from django.conf import settings

from .managers import CustomUserManager
from .time import TimestampedModel
from django.utils.translation import gettext_lazy as _


class CommonUser(AbstractUser, TimestampedModel):
    username = None
    name = models.CharField(max_length=400, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
     
    # @property
    # def token(self):
    #     return self._generate_jwt_token( )

    # def _generate_jwt_token(self):
    #     dt = datetime.now( ) + timedelta(days=60)
    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': dt.utcfromtimestamp(dt.timestamp())
    #         }, settings.SECRET_KEY, algorithm='HS256')
    #     return token
    
    class Meta:
        db_table = 'commonuser'
        
    def __str__(self):
        return self.email
    
    
# class CommonUser(AbstractUser):
#     username = None
#     name = models.CharField(max_length=400, null=True, blank=True)
#     email = models.EmailField(_('email address'), unique=True)
#     phone = models.CharField(max_length=400, null=True, blank=True)

#     LOGIN_EMAIL = 'email'
#     LOGIN_KAKAO = 'kakao'
#     LOGIN_NAVER = 'naver'
#     LOGIN_CHOICES = (
#         (LOGIN_EMAIL, 'email'),
#         (LOGIN_NAVER, 'naver'),
#         (LOGIN_KAKAO, 'kakao')
#     )

#     login_method = models.CharField(
#         max_length=6, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
#     )

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()
#     class Meta: 
#         db_table = 'commonuser' 
        
#     def __str__(self):
#         return self.email
    

# class FullUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CommonUser
#         fields = ['id', 'username', 'email', 'last_login',
#                   'date_joined', 'status', 'phone_number']

