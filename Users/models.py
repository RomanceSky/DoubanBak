# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Users(models.Model):
    Usersname = models.CharField(u'用户名', max_length=60, unique=True)
#    UserPassword = models.CharField(u'用户密码', max_length=60, unique=True)
    Usersemail = models.CharField(u'用户邮箱', max_length=60)
