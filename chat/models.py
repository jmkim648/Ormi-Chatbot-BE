from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=20)
    convention = models.CharField(max_length=100, null=True, blank=True, default='없음')

    def __str__(self):
        return f"채팅방 : {self.id}, 유저 : {self.user.email}"

class ChatMessage(models.Model):
    chatpost = models.ForeignKey(ChatPost, on_delete=models.CASCADE)
    is_user = models.BooleanField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"메시지 : {self.id} 채팅방 : {self.chatpost} 작성자 : {'User' if self.is_user else 'Chatbot'}"