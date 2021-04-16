from django.db import models
from django.contrib.auth.models import User
from users.models import Worker, Client
from organization.models import Organization

SERVICE_STATUS = (
        ('выполнена', 'выполнена'),
        ('в процессе', "в процессе"),
        ("не выполненна", "не выполненна")
    )

class Service(models.Model):  
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    name = models.CharField('name', max_length = 50, default='')
    comment = models.CharField('comment', max_length = 200, default='')

    class Meta: 
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class Service_rendered(models.Model):
    name = models.CharField('name', max_length = 20, default='')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    comment = models.CharField('comment', max_length = 200, default='')
    status = models.CharField(max_length=18, choices=SERVICE_STATUS, default="не выполненна")
    date = models.DateField('date', max_length=20, auto_now=True)

    class Meta: 
        verbose_name = 'Предоставленная услуга'
        verbose_name_plural = 'Предоставленные услуги'

    def __str__(self):
        return self.name +  ' [ ' + str(self.id)+ ' ]'

        
class Documentation(models.Model):
    Service_rendered = models.ForeignKey(Service_rendered, on_delete=models.CASCADE, null=True)
    name = models.CharField('name_documents', max_length = 200, default='')
    doc = models.FileField(upload_to='uploads/')

    class Meta: 
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name