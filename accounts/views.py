from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
