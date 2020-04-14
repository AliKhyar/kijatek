from django.contrib import admin
from django.apps import apps
# Register your models here.

myapp = apps.get_app_config('core')
admin.site.register(myapp.get_models())
