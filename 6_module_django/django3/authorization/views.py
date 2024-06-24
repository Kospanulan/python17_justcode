from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response

from authorization.serializers import UserRegisterSerializer, UserLoginSerializer


# Регистрация, Аутентификация, Авторизация


class RegisterAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer

    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.save(password=hashed_password)

