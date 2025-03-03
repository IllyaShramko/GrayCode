from django.shortcuts import render, redirect
from django.http import HttpRequest
from create_qrc.models import QRcodes
from django.utils import timezone
from user.models import Profile
import os
# Create your views here.

def render_my_qrs(request: HttpRequest):
    sorting_type = "a-z"
    popup_alert= False
    delete_name = None
    delete_qrcode = 0
    if request.method == "POST":
        
        if 'deleteqr' in request.POST.get('button'):
            profiles = Profile.objects.filter(user_id= request.user.id)
            profile = profiles[0]
            profile.qrcodes_created -= 1
            profile.save()
            name_delete = QRcodes.objects.get(id= request.POST.get("button").split('-')[-1]).name
            os.remove(os.path.abspath(__file__ + "/../../media/images/qrcodes/" + request.user.username + "/" + name_delete + '.png'))
            QRcodes.objects.get(id=request.POST.get("button").split('-')[-1]).delete()
        elif request.POST.get('button') == "safe":
            popup_alert = False
        elif 'delete' in request.POST.get('button'):
            delete_qrcode = request.POST.get('button').split('-')[-1]
            popup_alert = True
            delete_name = request.POST.get('button').split('-')[-2]
        else:
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

    return render(request, "my_qrs/my_qrs.html", context={"is_auth": True, "username": request.user, "qrcodes": qrcodes, 'popup_alert': popup_alert, 'delete_name': delete_name,'delete_qrcode':delete_qrcode})



def redirect_qrcode(request: HttpRequest, pk):
    QRcode = QRcodes.objects.get(pk=pk)
    url = QRcode.url
    date_delete = QRcode.date_delete
    
    if QRcode.user.subscribe == "base":
        if date_delete < timezone.now():
            return render(request, 'my_qrs/error_qrcode.html', context={
                "error_qrcode": 'time'
            })
    elif QRcode.user.subscribe.id < QRcode.subscribe_created.id:
        return render(request, 'my_qrs/error_qrcode.html', context={
            "error_qrcode": 'sub', "is_auth": True, "username": request.user,
            'sub': {
                "current": Profile.objects.get(user= request.user).subscribe,
                "created": QRcode.subscribe_created
            }
        })
    print(url)
    return redirect(url)