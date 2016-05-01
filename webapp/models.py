from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mobile(models.Model):
    skuid = models.CharField(max_length=50,primary_key=True)
    url = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    price = models.FloatField()
    listDate = models.CharField(max_length=40)
    inputType = models.CharField(max_length=40)
    isSmart = models.CharField(max_length=10)
    osVersion = models.CharField(max_length=200)
    mbROM = models.CharField(max_length=100)
    scrSize = models.CharField(max_length=200)
    fenbianlv = models.CharField(max_length=100)
    hvGPS = models.CharField(max_length=10)
    reCamera = models.CharField(max_length=50)
    prCamera = models.CharField(max_length=50)
    hvWiFi = models.CharField(max_length=10)
    hvBlue = models.CharField(max_length=10)
    battery = models.CharField(max_length=200)
    mbSize = models.CharField(max_length=200)
    mbWeight = models.CharField(max_length=200)