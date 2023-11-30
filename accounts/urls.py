from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, LogoutView, UserCreateAPIView, UserViewSet

app_name = 'accounts'

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]