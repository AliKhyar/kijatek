from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'core'  # here for namespacing of urls.

urlpatterns = [
    path("", views.home_page, name="home"),
    path("search", views.search, name="search"),
    path("search_info:<bac_plus>+<department>+<city>", views.search_info, name="search_info"),
]