from django.contrib import admin
from .models import Chats, Attachments

# Register your models here.
admin.site.register(Chats)
admin.site.register(Attachments)