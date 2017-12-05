# -*- coding: utf-8 -*-
from django.conf.urls import url
from .models import *
from .views import *

urlpatterns = [
    url(r'^news/$', newsView,name='news'),    
    url(r'^news/list/$', newslistView, name="newslist"),
]       
