from rest_framework import serializers
from .models import MainCategory, SubCategory, Sender, Recipient, \
                    DocumentForm, Document, DocumentChat
                    
class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
        )
        model = MainCategory
        
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'main'
        )
        model = SubCategory
        
class DocumentFormSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'category',
            'content',
        )
        model = DocumentForm
        
class DocumentSerializer(serializers.ModelSerializer):
    contents = serializers.JSONField()
    class Meta:
        fields = (
            'id',
            'user',
            'category',
            'sender',
            'recipient',
            'contents',
            'title',
            'file_path',
            'created_at',
            'updated_at',
            'deleted_at',
        )
        model = Document

class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'sender_name',
            'sender_address',
            'sender_phone',
        )
        model = Sender
        
class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'recipient_name',
            'recipient_address',
            'recipient_phone',
        )
        model = Recipient
        
class DocumentChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'category',
            'message',
        )
        model = DocumentChat


class DocumentPostSerializer(serializers.Serializer):
    sender = serializers.IntegerField()
    recipient = serializers.IntegerField()
    subname = serializers.CharField()
    main = serializers.IntegerField()
    context = serializers.DictField()
    user_id = serializers.IntegerField()
    
class DocumentDetailGetSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    
class DocumentDetailPatchSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    sender = serializers.DictField()
    recipient = serializers.DictField()
    title = serializers.CharField()
    contents = serializers.DictField()