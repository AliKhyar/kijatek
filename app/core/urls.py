from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'core'  # here for namespacing of urls.

urlpatterns = [
    path("", views.home_page, name="home"),
    path("search/data=<bac_plus>+<discipline>+<city>", views.search_info, name="search_info"),
    path("establishments/data=<establishment_id>", views.search_establishment, name="search_establishment"),
    path("all-establishments/", views.all_establishments, name="all_establishments"),
    path("establishments/departments/data=<establishment_id>+<department_id>", views.search_department, name="search_department"),
    path("establishments/all-departments/", views.all_departments, name="all_departments"),
    path("test", views.test, name="test"),
]