
#_*_coding:utf-8_*_
from django.db import models
"""
---------------
"""
class reading(models.Model):

    Bookname = models.CharField(u'书名', max_length = 60)
    Author = models.CharField(u'作者', max_length = 60) 
    ISBN = models.CharField(u'ISBN', max_length = 60)
    Category = models.CharField(u'类别', max_length = 60, null = True,blank = True) 
    Picture = models.ImageField(upload_to = 'pictures',  null = True,blank = True) 
    Grade = models.IntegerField(u'评分', default = 0) 
    Ranking = models.DateTimeField(u'上榜时间', auto_now_add = True, null = True,blank = True) 
    Price = models.CharField(u'价格',max_length = 60, default = 0)
    Postage = models.CharField(u'邮费', max_length = 60, default = 0)
    Abstract = models.CharField(u'简介', max_length = 130) 
    Comment = models.CharField(u'书评', max_length = 130, null = True,blank = True) 
    Quantity =  models.IntegerField(u'数量', default = 0,  null = True)
    createTime = models.DateTimeField(u'创建时间', auto_now_add = True, null = True,blank = True)
    website = models.URLField(max_length=200)
