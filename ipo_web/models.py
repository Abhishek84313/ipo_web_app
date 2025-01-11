from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class IPOInfo(models.Model):
    company_name = models.CharField(max_length=255)
    ipo_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)