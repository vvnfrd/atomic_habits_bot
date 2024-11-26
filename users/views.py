from rest_framework import generics
from users.serializers import RegisterSerializer
from users.models import User


"""Сервис пользователя"""


class RegisterAPIView(generics.CreateAPIView):
    """Register account"""
    serializer_class = RegisterSerializer
    queryset = User.objects.all()