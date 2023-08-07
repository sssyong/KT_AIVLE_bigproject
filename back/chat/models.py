from django.db import models
from django.conf import settings
from doc.models import MainCategory
# Create your models here.


class ClassificationChat(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    message = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'classification_chat'
        
class LawgptChat(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'lawgpt_chat'
