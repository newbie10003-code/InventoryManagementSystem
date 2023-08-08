from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if(request.method=='POST'):
        uname = request.POST['username']
        name = request.POST['Name']
        email = request.POST['Email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        if(pwd1!=pwd2):
            return HttpResponse("Passwords do not match")
        user = User.objects.create(username=uname, name=name, email=email, password=pwd1)
        user.save()
        return HttpResponse("User created successfully")
    return render(request, 'signup.html')


def login(request):
    if(request.method=='POST'):
        uname = request.POST['username']
        user = User.objects.all().filter(username=uname)
        if(user):
            return HttpResponse("User already exists")
        else:
            return HttpResponse("User does not exist")
    return render(request, 'login.html')