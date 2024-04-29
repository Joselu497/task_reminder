from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .serializers import UserLoginSerializer
from .serializers import UserRegisterSerializer
from .permissions import IsAdmin

"""
ViewSet for managing User model instances.    
This ViewSet is only accessible to users with the 'IsAdmin' permission.
"""
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdmin, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
View for user login.
Uses the TokenObtainPairView from the rest_framework_simplejwt library
to generate access and refresh tokens for authenticated users.
"""
class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    
"""
View for user registration
"""
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer
    