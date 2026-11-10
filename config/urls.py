from django.urls import path

from .api import health_check


urlpatterns = [
    path("api/health/", health_check),
]