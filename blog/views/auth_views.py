
from django.shortcuts import render, redirect
from ..models import CustomUser as User
from django.contrib.auth import authenticate,login as LOGIN

def register(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_pic = request.FILES.get("image")
        user = User.objects.create(
            username = username, 
            email = email, 
            user_pic = user_pic

        )
        user.set_password(password)
        user.save()
        return redirect("login")
    return render(request,'auth/register.html')

def login(request):
    if request.method == 'POST': 
        username = request.POST.get("username") 
        password = request.POST.get("password") 
        user = authenticate(request,username=username,password=password) 
        if user is not None:
            LOGIN(request,user)
            return redirect("home")
        else:
            return redirect("login")
    return render(request,'auth/login.html')

