from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    seller_of_the_month = models.BooleanField(default=False)
    hire_date = models.DateField(datetime.now, blank=True)

    def __str__(self):
        return self.name 


