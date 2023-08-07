from rest_framework import serializers
from .models import Board
from accounts.serializers import UserSerializer

class BoardSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'updated_at',
            'deleted_at',
        )
        model = Board

class BoardUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'updated_at',
            'deleted_at',
        )
        model = Board