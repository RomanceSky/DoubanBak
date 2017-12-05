from django.shortcuts import render

# Create your views here.


def newsView(request):
    return render(request,'news.html')

def newslistView(request):
    #return render(request,'newslist.html')
    return render(request, 'Index.html')
