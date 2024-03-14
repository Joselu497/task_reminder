from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserLoginView, UserRegistrationView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),

    path('auth/register/', UserRegistrationView.as_view(), name='user-register'),
    path('auth/login/', UserLoginView.as_view(), name='user-login'),
]