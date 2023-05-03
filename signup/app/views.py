from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import user


# Create your views here.
def index(request):
    return render(request,'index.html')

def ragistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        DOB = request.POST['DOB']
        password = make_password(request.POST['password'])
        if user.objects.filter(email=email).exists():
            messages.error(request,"Email alrady exists")
        elif user.objects.filter(contact=contact).exists():
            messages.error(request,"contact alrady exists")   
        else:
            user.objects.create(name=name,email=email,
                                contact=contact,DOB=DOB,
                                password=password)     
        return redirect('/Login/')
    
def Login(request):
    return render(request,'Login.html')

def Login_page(request):
    if request.method == 'POST':
        email = request.POST['Email']
        User_password = request.POST['Password']
        if user.objects.filter(email=email).exists():
            obj = user.objects.get(email=email)
            Password = obj.password
            if check_password(User_password,Password):
                return redirect('/table/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('Email is not registerd')    

def table(request):
    return render(request,'table.html')