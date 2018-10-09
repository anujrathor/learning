from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    DOB = models.DateField(null=True,blank=True)
    mobile_no = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=250,blank=True)





