
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import  login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
#login_required(login_url=reverse_lazy("read-create"))
def userCreateView(request):
    return render(request,'loginIndex.html')
