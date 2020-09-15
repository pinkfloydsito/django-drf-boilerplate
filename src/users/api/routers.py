
from users.api import viewsets
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'', viewsets.UserViewSet)
