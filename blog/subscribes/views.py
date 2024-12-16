from django.shortcuts import render

# Create your views here.

def render_subs(request):
    return render(request, "subscribes/subs.html", context={"is_auth": True})
