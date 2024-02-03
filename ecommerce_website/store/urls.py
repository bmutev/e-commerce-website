from django.urls import path

from . import views

urlpatterns = [
    # Empty string because this is the homepage
    path('', views.store, name='store'),
]
