from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import  login_required
# Create your views here.
#@login_required(login_url=reverse_lazy("read-create"))
def readCreateView(request):
    return render(request, 'readCreate.html')
    
