from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class IPOInfo(models.Model):
    logo = models.URLField(max_length=500, null=True, blank=True)
    ipo_date = models.DateField()
    company_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
