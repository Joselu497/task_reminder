from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .serializers import UserLoginSerializer
from .serializers import UserRegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer
    