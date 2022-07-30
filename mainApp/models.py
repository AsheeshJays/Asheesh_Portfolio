from email import message
from django.db import models

class Contact(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class project(models.Model):
    pid = models.AutoField(primary_key=True)
    pName = models.CharField(max_length=255)
    pUrl = models.CharField(max_length=500)
    pImage = models.ImageField(upload_to='images/',default=None,null=True,blank=True)

    def __str__(self):
        return self.pName

class Hire(models.Model):
    Hid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
