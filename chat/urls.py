from django.urls import path
from .views import ChatListView, ChatDetailView

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view(), name='chat_list'),
    path('<int:chat_pk>/', ChatDetailView.as_view(), name='chat-detail'),
]