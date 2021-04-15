from django.db import models
from django.contrib.auth.models import User




class Organization(models.Model):
    name = models.CharField('name', max_length = 200, default='')
    activity = models.CharField('activity', max_length = 500, default='')

    class Meta: 
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
    
    def __str__(self):
        return self.name

class Office_Organization(models.Model):
    organization = models.ForeignKey(Organization, on_delete = models.CASCADE)
    addres = models.CharField('addres', max_length = 50, default='')
    phone_number = models.CharField('phone number', max_length = 20, default='')

    class Meta: 
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'
    
    def __str__(self):
        return self.addres

