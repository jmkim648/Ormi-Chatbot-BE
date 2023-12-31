from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'board'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:post_pk>/', PostDetailView.as_view(), name='post_detail'),
]