from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    '''
    SignupSerializer
    '''
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta(object):
        model = User
        fields = ['email', 'password', 'password2', 'nickname']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "비밀번호가 서로 다릅니다."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('email'),
            nickname=validated_data.get('nickname'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    '''
    Login Serializer
    '''
    class Meta(object):
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'email': {'validators': []}, 
        }

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email:
            raise serializers.ValidationError('이메일을 입력해주세요.')
        
        if not password:
            raise serializers.ValidationError('비밀번호를 입력해주세요.')

        user = authenticate(request=self.context.get('request'),
            username=email, password=password
        )
        if user is None:
            raise serializers.ValidationError('아이디나 비밀번호가 올바르지 않습니다.')
        
        if not user.is_active:
            raise serializers.ValidationError('휴면유저입니다.')
        
        return { "email": email, "password": password, "user":user }
    

class UserUpdateSerializer(serializers.ModelSerializer):
    '''
    User update Serializer(Profile)
    '''

    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=False)
    confirm_new_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['nickname', 'user_img', 'current_password', 'new_password', 'confirm_new_password']

    def validate(self, data):
        current_password = data.get('current_password')
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')

        if not current_password:
            raise serializers.ValidationError('현재 비밀번호를 입력해주세요.')

        user = authenticate(request=self.context.get('request'),
                            username=self.instance.email, password=current_password)

        if not user:
            raise serializers.ValidationError('현재 비밀번호가 올바르지 않습니다.')

        if new_password or confirm_new_password:
            if not new_password:
                raise serializers.ValidationError('새 비밀번호를 입력해주세요.')

            if new_password != confirm_new_password:
                raise serializers.ValidationError('새 비밀번호와 확인 비밀번호가 일치하지 않습니다.')

            validate_password(new_password, user=self.instance)
        return data

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.user_img = validated_data.get('user_img', instance.user_img)

        new_password = validated_data.get('new_password')
        if new_password:
            instance.set_password(new_password)

        instance.save()
        return instance