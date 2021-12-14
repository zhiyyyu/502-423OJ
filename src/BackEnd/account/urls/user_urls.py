from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.views import user_views

router = DefaultRouter()
