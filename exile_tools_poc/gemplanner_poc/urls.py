"""
high level support for doing this and that.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
