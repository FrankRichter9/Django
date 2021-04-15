from django.contrib import admin


from .models import Client, Worker, Admin, Office_MFC


admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Admin)
admin.site.register(Office_MFC)
