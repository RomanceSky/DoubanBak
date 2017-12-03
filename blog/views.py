#coding=utf-8
from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response

from Bean.models import BlogsPost
# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})

