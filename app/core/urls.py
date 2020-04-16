from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'core'  # here for namespacing of urls.

urlpatterns = [
    path("", views.home_page, name="home"),
    path("test", views.test, name="test"),
    path("search_info/data=<bac_plus>+<discipline>+<city>", views.search_info, name="search_info"),
]