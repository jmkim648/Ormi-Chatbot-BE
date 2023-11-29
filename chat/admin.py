from django.contrib import admin
from .models import ChatPost, ChatMessage

admin.site.register(ChatPost)
admin.site.register(ChatMessage)