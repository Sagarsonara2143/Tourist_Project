from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.PositiveSmallIntegerField()
    address = models.TextField(max_length = 100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.first_name + "" + self.last_name