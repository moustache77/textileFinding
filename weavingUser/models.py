from __future__ import unicode_literals
from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=20, null=False)
    sex = models.CharField(max_length=2)
    registerTime = models.DateTimeField(max_length=30)
    birthday = models.DateField(max_length=30)
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.username, self.password,self.phone,self.registerTime
