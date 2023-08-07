from rest_framework import serializers
from .models import ClassificationChat, LawgptChat


    
class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'category',
            'message',
            'answer',
            'created_at',
        )
        model = ClassificationChat
        
class LawgptSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'message',
            'answer',
            'created_at',
        )
        model = LawgptChat