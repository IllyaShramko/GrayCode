from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def render_login(request):  
    return render(request, "user/login.html", context={"is_auth": False})

def render_registration(request):
    confirm = False
    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            try:
                User.objects.create_user(username= username, password= password)
                confirm = True
            except:
                error = 'username_error'
        else:
            error = 'password_error'
        print(confirm)
    return render(request, "user/registration.html", context={"is_auth": False, "confirm": confirm, "error": error})    