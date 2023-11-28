from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, CreatePostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly, IsManagerOrReadOnly

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePostSerializer
        return PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsManagerOrReadOnly]