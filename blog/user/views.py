from django.shortcuts import render

# Create your views here.


def render_login(request):  
    return render(request, "user/login.html", context={"is_auth": False})

def render_registration(request):
    confirm = False
    if request.method == "POST":
        confirm = True
        print("FPOGDKF[SKGDOFG]")
    return render(request, "user/registration.html", context={"is_auth": False, "confirm": confirm})    