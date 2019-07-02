# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product,Balance

admin.site.register(Product)
admin.site.register(Balance)