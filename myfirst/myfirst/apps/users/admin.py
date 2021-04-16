from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Client, Worker, Admin, Office_MFC

class AdminAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('user','full_name','phone_number')
    search_fields = ['full_name','phone_number']

class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('user','full_name','phone_number', 'address', 'passport')
    search_fields = ['full_name','phone_number','address', 'passport']

class Office_MFCAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('office_name','addres','phone_number')
    search_fields = ['office_name','addres','phone_number']

class WorkerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('user','full_name','phone_number', 'office', 'window_number')
    search_fields = ['full_name','phone_number', 'office__office_name', 'window_number']


admin.site.register(Client, ClientAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Office_MFC, Office_MFCAdmin)
