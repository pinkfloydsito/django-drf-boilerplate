from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics

from users.api.serializers import UserSerializer
from users.models import User


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

