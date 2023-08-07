from django.db import models
from django.conf import settings 
        
class MainCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    
    class Meta: 
        db_table = 'main_category' 
        
        
class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    main = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    
    class Meta: 
        db_table = 'sub_category' 
        
        
class Sender(models.Model):
    id = models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=50)
    sender_address = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=50)
    
    class Meta: 
        db_table = 'sender' 
        
        
class Recipient(models.Model):
    id = models.AutoField(primary_key=True)
    recipient_name = models.CharField(max_length=50)
    recipient_address = models.CharField(max_length=100)
    recipient_phone = models.CharField(max_length=50)
    
    class Meta: 
        db_table = 'recipient' 
        

class DocumentForm(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    
    class Meta: 
        db_table = 'document_form'
        
        
class Document(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    contents = models.CharField(max_length=3000)
    file_path = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    
    class Meta: 
        db_table = 'document' 
        
        
class DocumentChat(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    
    class Meta: 
        db_table = 'document_chat' 
        