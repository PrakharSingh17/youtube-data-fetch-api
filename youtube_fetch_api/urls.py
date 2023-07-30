"""youtube_fetch_api URL Configuration
"""
from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.YoutubeItems.as_view())
]
