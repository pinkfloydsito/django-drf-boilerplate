from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from helpers.health_check import health_check

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('users.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Enables the DRF browsable API page
    path("health_check/", health_check, name="health_check"),
]

if settings.ENVIRONMENT == "development":
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
