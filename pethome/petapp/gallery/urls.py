# posts/urls.py
from django.urls import path

from .views import ImageList

urlpatterns = [
    path('',ImageList, name='home'),
]