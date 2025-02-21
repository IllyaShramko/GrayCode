from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def render_login(request):  
    error = False
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request = request,username = username, password = password)
        if user:
            login(request = request, user = user)
            print(request.user)
            return redirect("/")
        else:
            error = True
    return render(request, "user/login.html", context={"is_auth": False, "error": error, 'username': request.user})

def render_registration(request):
    confirm = False

    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            try:
                # User.objects.create_user(username= username, password= password)
                Profile.objects.create(user= User.objects.create_user(username= username, password= password))
                
                confirm = True
            except Exception as e:
                print(e)
                error = 'username_error'
        else:
            error = 'password_error'
        print(confirm)
    return render(request, "user/registration.html", context={"is_auth": False, "confirm": confirm, "error": error, 'username': request.user})    
# gl hf
def logout_user(request):
    logout(request)
    return redirect("/")