from django.urls import path, include
from users.api import viewsets
from users import views
from users.api.routers import router

urlpatterns = [
    path('account/register/', views.UserCreate.as_view()),
    path('users/', include(router.urls)),
]
