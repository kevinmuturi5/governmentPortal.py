# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from accounts import *

from django.dispatch import receiver
from django.db.models.signals import post_save


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.IntegerField(default = 0)
    def __str__(self):
        return str(self.user)


def craeteBalance(sender, instance, created, **kwargs):
    balanc,created = Balance.objects.get_or_create(user=instance,balance=10)
    balanc.save()
post_save.connect(craeteBalance, sender=settings.AUTH_USER_MODEL)    


 

        
       
    
