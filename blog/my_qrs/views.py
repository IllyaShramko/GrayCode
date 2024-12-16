from django.shortcuts import render

# Create your views here.
def render_my_qrs(request):
    return render(request, "my_qrs/my_qrs.html", context={"is_auth": True})
