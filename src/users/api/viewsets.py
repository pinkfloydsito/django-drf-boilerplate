from users.models import User
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
