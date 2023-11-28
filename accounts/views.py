from datetime import timedelta
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from .serializers import SignupSerializer, LoginSerializer, UserUpdateSerializer


class LoginView(TokenObtainPairView):
    '''
    Login
    '''
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }, status=status.HTTP_200_OK)
    

class LogoutView(APIView):
    '''
    Logout
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = RefreshToken(request.data["refresh"])
            refresh_token.set_exp(timedelta(days=1))
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserCreateAPIView(CreateAPIView):
    '''
    User Create
    '''
    serializer_class = SignupSerializer


class UserViewSet(ModelViewSet):
    '''
    User RUD
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request):
        user = self.get_object()
        data = {
            'email': user.email,
            'username': user.username,
        }
        return Response(data)
    
    def update(self, request):
        user = self.get_object()
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)

        if request.user != user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request):
        user = self.get_object()

        if request.user != user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


signup = UserCreateAPIView.as_view()
login = LoginView.as_view()
logout = LogoutView.as_view()