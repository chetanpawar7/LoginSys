from django.shortcuts import render,redirect
from .models import NewUser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        username = request.POST.get('emailid')
        email = request.POST.get('emailid')
        password = request.POST.get('password')
        confirm_pass =request.POST.get('confirm_pass')
        if password != confirm_pass:
            return HttpResponse('Passwords do not match')
        else:
            usr = User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
            
            usr.save()

            return redirect('loginuser/')

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('emailid')
        password = request.POST.get('password')
        
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            return HttpResponse('user is not authenticated')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('registeruser')

@login_required
def main(request):
    users = User.objects.all()
    context ={
        "users":users
    }
    return render(request, 'main.html',context)

