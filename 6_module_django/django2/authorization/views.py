from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, views
from rest_framework.response import Response

from authorization.serializers import UserRegisterSerializer, UserLoginSerializer


# Регистрация, Аутентификация, Авторизация


class RegisterAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.save(password=hashed_password)


# session authentication:
class LoginAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user is not None:
            login(request, user)
            return Response(
                {'detail': 'Login successful'},
                status=status.HTTP_200_OK
            )


class LogoutAPIView(views.APIView):

    def post(self, request, *args, **kwrgs):
        logout(request)
        return Response(
            {'detail': 'Logout successful'},
            status=status.HTTP_200_OK
        )
