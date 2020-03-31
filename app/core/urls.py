from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'core'  # here for namespacing of urls.

urlpatterns = [
    path("", views.index, name="index"),
]