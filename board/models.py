from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

def post_thumbnail_path(instance, filename):
    return f'post_thumbnails/post_{instance.post.id}/{filename}'


class Post(models.Model):
    category_choices = [
        ('잡담', '잡담'),
        ('공지', '공지'),
        ('질문', '질문'),
    ]

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    head_image = models.ImageField(upload_to=post_thumbnail_path, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=10, choices=category_choices)
    viewcount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    comment_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'작성자 : {self.user.nickname} 내용 : {self.content}'