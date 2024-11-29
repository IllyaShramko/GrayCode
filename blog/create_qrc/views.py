from django.shortcuts import render

# Create your views here.

def render_create_qrc(request):
    return render(request, "create_qrc/qrc.html")