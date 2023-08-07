# main/views.py

from datetime import datetime
from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import MainCategory, SubCategory, Sender, Recipient, \
                    DocumentForm, Document, DocumentChat

from .serializers import SenderSerializer, RecipientSerializer, DocumentChatSerializer, \
    MainCategorySerializer,SubCategorySerializer,\
        DocumentFormSerializer,DocumentSerializer,\
            DocumentPostSerializer, DocumentDetailGetSerializer, DocumentDetailPatchSerializer\
                
from accounts.models import CommonUser
import requests
from .makeDocument import makedocument, patchDocument


    
class CreateDocumentChat(generics.ListCreateAPIView):
    queryset = DocumentChat.objects.all()
    serializer_class = DocumentChatSerializer
    

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    
class CreateDocument(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_class = CustomPagination   
    
    

class ListUserDocument(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = DocumentSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Document.objects.filter(user_id=user, deleted_at=None)
        else:
            return Document.objects.none()
        
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Document.objects.filter(user=user, deleted_at=None)
    #     else:
    #         return Document.objects.none()
    
    # def post(self, request, *args, **kwargs):
    #     serializer_class = DocumentPostSerializer
        
    #     request_sender = self.request.sender
    #     request_recipient = self.request.recipient
        
    #     sender_data = Sender.objects.get(id = request_sender)
    #     recipient_data = Recipient.objects.get(id = request_recipient)
        
    #     context = self.request.context
        
    
    # def put(self, request, *args, **kwargs):
    #     request_sender = self.request.sender
    #     request_recipient = self.request.recipient
        
    #     sender_data = Sender.objects.get(id = request_sender)
    #     recipient_data = Recipient.objects.get(id = request_recipient)
    
    
        

class ListUserDocumentChat(generics.ListAPIView):
    serializer_class = DocumentChatSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return DocumentChat.objects.filter(user_id=user)
        else:
            return DocumentChat.objects.none()

            
    
# class DetailDocument(generics.RetrieveUpdateAPIView):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
    
    # def update(self):
    #     instance = self.get_object()
    #     instance.deleted_at = timezone.now()
    #     instance.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class DeleteDocument(generics.RetrieveUpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def perform_update(self, serializer):
        serializer.save(delete_at=datetime.now())
    
    
class ListSender(generics.ListCreateAPIView):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer

class ListRecipient(generics.ListCreateAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    

class ListMainCategory(generics.ListCreateAPIView):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    
class ListSubCategory(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
    
    
class DetailMainCategory(generics.RetrieveUpdateAPIView):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    
class DetailSubCategory(generics.RetrieveUpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
class CreateDocumentForm(generics.ListCreateAPIView):
    queryset = DocumentForm.objects.all()
    serializer_class = DocumentFormSerializer

class Documentcreate(APIView):
    
    # def get(self, request):
    #     serializer = DocumentSerializer(Document.objects.all())
    #     return Response(serializer.data, status=status.HTTP_200_OK)
        # user = request.user
        # if user.is_authenticated:
        #     serializer = DocumentSerializer(Document.objects.filter(user=user, deleted_at=None))
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     serializer = DocumentSerializer(Document.objects.all())
        #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DocumentPostSerializer(data = request.data)
        if serializer.is_valid():
            request_sender = serializer.data['sender']
            request_recipient = serializer.data['recipient']
            request_subcategory = serializer.data['subname']
            request_maincategory = serializer.data['main']
            subcategory_data = SubCategory.objects.get(main_id = request_maincategory, 
                                                       name = request_subcategory)
            sender_data = Sender.objects.get(id = request_sender)
            recipient_data = Recipient.objects.get(id = request_recipient)
            user_id = serializer.data['user_id']
            user = CommonUser.objects.get(id = user_id)
            user_id = user.id
            context = serializer.data['context']
            content, pdflocation, title = makedocument(sender_data, recipient_data, context, \
                subcategory_data.name, request_maincategory, user_id)
            
            
            serializer_data = {'user': user_id, 'category': subcategory_data.id,
                               'contents': content, 'recipient': request_recipient,
                               'sender':request_sender, 'file_path': pdflocation, 'title': title}
            
            serializer = DocumentSerializer(data = serializer_data)
            if serializer.is_valid():
                serializer.save()
                response_data = {'pdf': pdflocation}
            
                return Response(response_data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    
class SenderPost(APIView):
    def post(self, request):
        serializer = SenderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_sender = Sender.objects.filter(sender_name = serializer.data['sender_name'],
                                                 sender_address =  serializer.data['sender_address'],
                                                 sender_phone = serializer.data['sender_phone'])
            response_sender_last = response_sender.last()
            response_data = {'sender' : response_sender_last.id}
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class RecipientPost(APIView):
    def post(self, request):
        serializer = RecipientSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            response_recipient = \
                Recipient.objects.filter(recipient_name = serializer.data['recipient_name'],
                                         recipient_address =  serializer.data['recipient_address'], 
                                         recipient_phone = serializer.data['recipient_phone'])
            response_recipient_last = response_recipient.last()
            response_data = {'recipient' : response_recipient_last.id}
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetailDocument(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        if request.user:
            other_app_url = 'http://127.0.0.1:8000/accounts/authVerify/'
            request_data = {"token" : request.auth}
            response = requests.post(other_app_url, data=request_data)
            response_json = response.json()
            
            docmnt =  Document.objects.get(id = pk)
            if docmnt.user_id != response_json['user_id']:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            send = Sender.objects.get(id = docmnt.sender_id)
            rect = Recipient.objects.get(id = docmnt.recipient_id)
            sender_data = {'sender_name' : send.sender_name, 'sender_address':send.sender_address,
                            'sender_phone':send.sender_phone}
            recipient_data = {'recipient_name' : rect.recipient_name, 'recipient_address':rect.recipient_address,
                            'recipient_phone':rect.recipient_phone}
            response_data = {'category':docmnt.category_id ,'title' : docmnt.title, 'sender' : sender_data, 'recipient': recipient_data,
                            'contents': eval(docmnt.contents)}
            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        serializer = DocumentDetailPatchSerializer(data = request.data)
        
        print(request.data)
        
        if serializer.is_valid():
            docmnt =  Document.objects.get(id = pk)
            if docmnt.user_id != serializer.data['user_id']:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
            send = Sender.objects.get(id = docmnt.sender_id)
            rect = Recipient.objects.get(id = docmnt.recipient_id)
            
            send.sender_name = serializer.data['sender']['sender_name']
            send.sender_address = serializer.data['sender']['sender_address']
            send.sender_phone = serializer.data['sender']['sender_phone']
            
            rect.recipient_name = serializer.data['recipient']['recipient_name']
            rect.recipient_address = serializer.data['recipient']['recipient_address']
            rect.recipient_phone = serializer.data['recipient']['recipient_phone']
            
            send.save()
            rect.save()
            documentsub = SubCategory.objects.get(id = docmnt.category_id)
            content, pdfpath, title = patchDocument(send, rect, serializer.data['contents'], documentsub.name, documentsub.main_id,
                                                    serializer.data['user_id'], pk, serializer.data['title'])
            
            
            docmnt.contents = content
            docmnt.file_path = pdfpath
            docmnt.title = title
            
            docmnt.save()
            
            response_data = {'pdf': pdfpath}
            
            
            return Response(response_data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if request.user:
            other_app_url = 'http://127.0.0.1:8000/accounts/authVerify/'
            request_data = {"token" : request.auth}
            response = requests.post(other_app_url, data=request_data)
            response_json = response.json()
            
            docmnt =  Document.objects.get(id = pk)
            if docmnt.user_id != response_json['user_id']:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            docmnt.deleted_at = datetime.today()
            
            docmnt.save()
            
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class DownloadPdf(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        if request.user:
            other_app_url = 'http://127.0.0.1:8000/accounts/authVerify/'
            request_data = {"token" : request.auth}
            response = requests.post(other_app_url, data=request_data)
            response_json = response.json()
            docmnt =  Document.objects.get(id = pk)
            
            f = open(docmnt.file_path, 'rb')
            pdfFile = File(f)
            response = HttpResponse(pdfFile.read(), content_type = 'application/pdf')
            response['Content-Disposition'] = 'attachement;'
            return response
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        