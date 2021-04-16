from django.contrib import admin

from .models import Service_rendered, Service, Documentation
from import_export.admin import ImportExportModelAdmin

def make_published(modeladmin, request, queryset):
    queryset.update(status='выполнена')
make_published.short_description = "Сделать все выполненными"

class Service_renderedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('client','worker','service', 'status','date')
    list_filter = ['status', 'date']
    search_fields = ['client__full_name', 'worker__full_name', 'service__name']
    actions = [make_published]

class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('name', 'organization','worker','comment')
    search_fields = ['name', 'organization__name','worker__full_name','comment']

class DocumentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('Service_rendered', 'name','doc')
    search_fields = ['Service_rendered__name', 'name','doc']
    

    

admin.site.register(Service_rendered, Service_renderedAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Documentation, DocumentationAdmin)
