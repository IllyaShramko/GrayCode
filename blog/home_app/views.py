from django.shortcuts import render

# Create your views here.
def render_home(request):
    return render(request, "home_app/home_app.html", context= {"is_auth": False})