from django.shortcuts import render
from create_qrc.models import QRcodes
from user.models import Profile
# Create your views here.

def render_my_qrs(request):
    sorting_type = "a-z"
    if request.method == "POST":
        sorting_type = request.POST.get("sorting-type")
        print(sorting_type)
    
    if sorting_type == "a-z": 
        qrcodes = QRcodes.objects.filter(user_id= Profile.objects.filter(user_id= request.user.id)[0].id).order_by('name')
    elif sorting_type == "z-a":
        qrcodes = QRcodes.objects.filter(user_id= Profile.objects.filter(user_id= request.user.id)[0].id).order_by('-name')
    elif sorting_type == "from-today":
        qrcodes = QRcodes.objects.filter(user_id= Profile.objects.filter(user_id= request.user.id)[0].id).order_by('-date')
    elif sorting_type == "from-old":
        qrcodes = QRcodes.objects.filter(user_id= Profile.objects.filter(user_id= request.user.id)[0].id).order_by('date')
    print(qrcodes)
    return render(request, "my_qrs/my_qrs.html", context={"is_auth": True, "username": request.user, "qrcodes": qrcodes})
