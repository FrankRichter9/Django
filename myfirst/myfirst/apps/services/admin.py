from django.contrib import admin

from .models import Service_rendered, Service, Documentation


admin.site.register(Service_rendered)
admin.site.register(Service)
admin.site.register(Documentation)
