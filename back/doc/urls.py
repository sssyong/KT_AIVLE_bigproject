# doc/urls.py
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'doc'
urlpatterns = [
    # path("", views.index),
    path("chat/", views.CreateDocumentChat.as_view(), name='create-document-chat'),
    path("chat/user/", views.ListUserDocumentChat.as_view(), name='list-user-document-chat'),
    path("", views.CreateDocument.as_view(), name='create-document'),
    path("user/", views.ListUserDocument.as_view(), name='list-user-document'),
    
    path("create/", views.Documentcreate.as_view(), name='test-document'),
    path("sender/", views.SenderPost.as_view(), name='test-sender'),
    path("recipient/", views.RecipientPost.as_view(), name='test-recipient'),
    
    # path("id/<int:pk>/", views.DetailDocument.as_view(), name='datail-document'),
    path("id/<int:pk>/", views.DetailDocument.as_view(), name='datail-document'),
    path("pdf/<int:pk>/", views.DownloadPdf.as_view(), name='datail-document'),
    
    path("sender/list/", views.ListSender.as_view(), name='list-sender'),
    path("recipient/list/", views.ListRecipient.as_view(), name='list-recipient'),
    path("main/", views.ListMainCategory.as_view(), name='create-maincategory'),
    path("sub/", views.ListSubCategory.as_view(), name='create-subcategory'),
    path("form/", views.CreateDocumentForm.as_view(), name='create-documentform'),
    
    
    path("main/id/<int:pk>/", views.DetailMainCategory.as_view(), name='detail-maincategory'),
    path("sub/id/<int:pk>/", views.DetailSubCategory.as_view(), name='detail-subcategory'),
    
]