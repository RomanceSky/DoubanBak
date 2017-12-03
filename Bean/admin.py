# -*- coding: utf-8 -*-

from django.contrib import admin
 
# Register your models here.
from Bean import models
admin.site.register(models.userinfo)
admin.site.register(models.UserType)
