from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import PositiveIntegerField


class CutomUser(AbstractUser):
    addres=models.CharField(max_length=120,blank=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
    def __str__(self):
        return self.first_name



