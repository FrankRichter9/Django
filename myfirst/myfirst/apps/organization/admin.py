from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Organization, Office_Organization


class OrganizationInstanceInline(admin.TabularInline):
    model = Office_Organization

class OrganizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'activity')
    inlines = [OrganizationInstanceInline]






class Office_OrganizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('organization', 'addres', 'phone_number')
    search_fields = ['organization__name', 'addres', 'phone_number']
    

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Office_Organization, Office_OrganizationAdmin)
