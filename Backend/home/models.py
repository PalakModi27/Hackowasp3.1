from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class signup_detail(models.Model):
    Name=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    Blood_Group=models.CharField(max_length=100)
    Vaccine=models.CharField(max_length=100)