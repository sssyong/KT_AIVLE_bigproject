from django.contrib import admin

from .models import MainCategory, SubCategory, Sender, Recipient, \
                    DocumentForm, Document, DocumentChat

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Sender)
admin.site.register(Recipient)
admin.site.register(DocumentForm)
admin.site.register(Document)
admin.site.register(DocumentChat)