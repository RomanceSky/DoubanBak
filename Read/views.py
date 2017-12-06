from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import  login_required
# Create your views here.
#@login_required(login_url=reverse_lazy("read-create"))
def readCreateView(request, id):
    read = reading.objects.get(id=id)
    return render(request, 'readCreate.html', {'read':'read'})
    
