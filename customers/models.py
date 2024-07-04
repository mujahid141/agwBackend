from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.BigIntegerField(null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    membership = models.CharField(max_length=1, choices=[
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ], default='B')
    customer_image = models.ImageField(null=True,blank=True)
    def __str__(self) -> str:
        return self.user

class Address(models.Model):
    street = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    postal_code = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, )
    def __str__(self) -> str:
        return self.user