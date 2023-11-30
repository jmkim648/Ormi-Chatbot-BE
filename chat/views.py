from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import ChatPost, ChatMessage
from .serializers import ChatPostSerializer, ChatMessageSerializer
from .permissions import IsOwnerAndAuthenticated
from chatbot.utils.openAI_API import OpenAIAPI
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import throttle_classes

class ChatListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        chat_posts = ChatPost.objects.filter(user=request.user)
        serializer = ChatPostSerializer(chat_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ChatPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, chat_pk):
        chat_post = get_object_or_404(ChatPost, pk=chat_pk)

        if request.user != chat_post.user:
            return Response({"detail": "작성자만 삭제할 수 있습니다."},
                            status=status.HTTP_403_FORBIDDEN)

        chat_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@throttle_classes([UserRateThrottle])
class ChatDetailView(APIView):
    permission_classes = [IsOwnerAndAuthenticated]
    throttle_classes = [UserRateThrottle]
    throttle_scope = "post"

    def get(self, request, chat_pk):
        chat_post = get_object_or_404(ChatPost, pk=chat_pk, user=request.user)
        chat_messages = ChatMessage.objects.filter(chatpost=chat_post)
        serializer = ChatMessageSerializer(chat_messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, chat_pk):
        chat_post = get_object_or_404(ChatPost, pk=chat_pk, user=request.user)
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chatpost=chat_post, is_user=True)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        user_message = ChatMessage.objects.filter(chatpost=chat_post, is_user=True).order_by('-created_at').first()

        chatbot_response = OpenAIAPI.generate_response(user_message.content, chat_post.language, chat_post.convention)

        new_chatbot_message = ChatMessage.objects.create(
            chatpost=chat_post,
            is_user=False,
            content=chatbot_response
        )

        serializer = ChatMessageSerializer(ChatMessage.objects.filter(chatpost=chat_post).order_by('created_at'), many=True)
        serializer.data.append({
            'id': new_chatbot_message.id,
            'chatpost': chat_post.id,
            'is_user': False,
            'content': chatbot_response,
            'created_at': new_chatbot_message.created_at
        })

        return Response(serializer.data, status=status.HTTP_200_OK)