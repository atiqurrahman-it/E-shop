from django.db import models


class CustomerUserProfile(models.Model):
    first_name = models.CharField(max_length=52)
    last_name = models.CharField(max_length=52)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=52)
    password = models.CharField(max_length=502)
