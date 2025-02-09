from django.shortcuts import render
from create_qrc.models import QRcodes
# Create your views here.
def render_my_qrs(request):
    qrcodes = QRcodes.objects.filter(user_id= request.user.id)
    # print()
    return render(request, "my_qrs/my_qrs.html", context={"is_auth": True, "username": request.user, "qrcodes": qrcodes})
