from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mobile(models.Model):
    skuid = models.CharField(max_length=50,primary_key=True)
    url = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    price = models.FloatField()
    listDate = models.CharField(max_length=20)
    inputType = models.CharField(max_length=20)
    isSmart = models.CharField(max_length=10)
    osVersion = models.CharField(max_length=40)
    mbROM = models.CharField(max_length=100)
    scrSize = models.CharField(max_length=15)
    fenbianlv = models.CharField(max_length=40)
    hvGPS = models.CharField(max_length=10)
    reCamera = models.CharField(max_length=15)
    prCamera = models.CharField(max_length=15)
    hvWiFi = models.CharField(max_length=10)
    hvBlue = models.CharField(max_length=10)
    battery = models.CharField(max_length=60)
    mbSize = models.CharField(max_length=40)
    mbWeight = models.CharField(max_length=40)