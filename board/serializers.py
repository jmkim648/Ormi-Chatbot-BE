from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        if data.get('category') == '공지' and not self.context['request'].user.is_manager:
            raise serializers.ValidationError('공지글은 관리자만 작성할 수 있습니다.')
        return data
