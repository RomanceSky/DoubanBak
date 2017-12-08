#-*-coding:utf-8-*-
from django.contrib.auth.decorators import  login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from Read.models import *
#login_required(login_url=reverse_lazy("read-create"))
def userCreateView(request):
    Bookname = request.GET
    #if data['bookname']:
#        Bookname = reading.filter(Bookname=data['bookname'])
       # Bookname = data['bookname']
   # Bookname = name['bookname']
#    Bookname  = reading.objects.get(Bookname='12')
    return render(request,'usercreate.html')
#返回的值是bookname，因为我加了''    return render(request,'readCreate.html',{'Bookname':'Bookname'})                                                           
