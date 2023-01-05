from django.db import models
from django.db import models
from .models import*
 
class contacts(models.Model):
     name=models.CharField(max_length=50,null=True)
     email=models.CharField(max_length=50,null=True)
     phone_no=models.CharField(max_length=50,null=True)
     Message=models.CharField(max_length=50,null=True)
# Create your models here.
