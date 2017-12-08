from django.shortcuts import render

from Users.models import *
# Create your views here.
def UsersCreateView(request):
    UsersList = Users.objects.all()
    list = {}
    
    for item in UsersList:
        id = item.id
        Usersname = item.Usersname
        Usersemail = item.Usersemail
  #  UsersList = Users.objects.get(id=id)
    return render(request,'UsersCreate.html',{'UsersList':UsersList})

