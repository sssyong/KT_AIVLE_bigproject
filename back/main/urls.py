# main/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("doc/", include('doc.urls')),
    path("board/", include('board.urls')),
    path("accounts/", include('accounts.urls')),
    path("chat/", include('chat.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
