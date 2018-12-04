"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .recordbin.views import RecordViewSet, SourceViewSet, SourceTokenViewSet
from .core.jwt import urlpatterns as jwt_auth_urlpatterns
from .docs import urlpatterns as doc_urlpatterns
from .tableau import urlpatterns as tablea_urlpatterns


router = routers.DefaultRouter()
router.register("records", RecordViewSet)
router.register("sources", SourceViewSet)
router.register("tokens", SourceTokenViewSet)

urlpatterns = [
    path("api/v1/", include((router.urls, "records"), namespace="v1")),
    path("api/v1/auth/", include(jwt_auth_urlpatterns)),
    path("", admin.site.urls),
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    *doc_urlpatterns,
    *tablea_urlpatterns,
]
