from rest_framework import serializers
from .models import ChatPost, ChatMessage

class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatPost
        fields = ['user', 'created_at', 'language', 'convention']

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['chatpost', 'is_user', 'content', 'created_at']