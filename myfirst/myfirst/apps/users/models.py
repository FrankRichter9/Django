from django.db import models
from django.contrib.auth.models import User




class Client(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField('full name', max_length = 50, default='')
    address = models.CharField('address', max_length = 200, default='')
    passport = models.CharField('passport', max_length = 20, default='')
    phone_number = models.CharField('phone number', max_length = 20, default='')

    class Meta: 
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.full_name

class Office_MFC(models.Model):
    office_name = models.CharField('office name', max_length = 50, default='')
    addres = models.CharField('addres', max_length = 50, default='')
    phone_number = models.CharField('phone number', max_length = 20, default='')

    class Meta: 
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        return self.office_name

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    office = models.ForeignKey(Office_MFC, on_delete = models.CASCADE, null=True)
    full_name = models.CharField('full name', max_length = 50, default='')
    phone_number = models.CharField('phone number', max_length = 20, default='')
    window_number = models.CharField('window number', max_length = 10, default='')

    class Meta: 
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField('full name', max_length = 50, default='')
    phone_number = models.CharField('phone number', max_length = 20, default='')

    class Meta: 
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return self.full_name


