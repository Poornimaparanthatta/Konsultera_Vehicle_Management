from django.db import models

# Create your models here.

class vehicleDB(models.Model):
    Vehicle_Number=models.CharField(max_length=15,null=True,blank=True)
    Vehicle_Type=models.CharField(max_length=15,null=True,blank=True)
    Vehicle_Model=models.CharField(max_length=15,null=True,blank=True)
    Description=models.CharField(max_length=10000,null=True,blank=True)

class UserRegDB(models.Model):
    Username=models.CharField(max_length=15,null=True,blank=True)
    Password=models.CharField(max_length=15,null=True,blank=True)
