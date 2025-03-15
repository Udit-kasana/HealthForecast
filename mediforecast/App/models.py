from django.db import models
# from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=1000)
class Message(models.Model):
    value=models.CharField(max_length=1000000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user= models.CharField(max_length=1000000)
    room= models.CharField(max_length=1000000)
# Create your models here.
class Appoint(models.Model):
    Name=models.CharField(max_length=10000)
    Email=models.CharField(max_length=10000)
    Phone=models.CharField(max_length=10000)
    Doctor=models.CharField(max_length=10000)
    Date=models.CharField(max_length=10000)
    Time=models.CharField(max_length=10000)
    # MRNno=models.CharField(max_length=10000)

