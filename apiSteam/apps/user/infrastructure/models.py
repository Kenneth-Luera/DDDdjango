from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    ROL_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='user')
    STATE_ACCOUNT_CHOICES = [
        ('ACTIVE', 'Active'),
        ('SUSPENDIDO', 'Suspended'),
        ('BANNED', 'Banned')
    ]
    state_account = models.CharField(max_length=10, choices=STATE_ACCOUNT_CHOICES, default='ACTIVE')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nationality = CountryField(blank=True, null=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email