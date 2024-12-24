from django.shortcuts import render
import qrcode, os
# Create your views here.

def render_create_qrc(request):
    if request.method == "POST":
        name = request.POST.get('name')
        url = request.POST.get('url')
        fill_color = request.POST.get('fill_color')
        back_color = request.POST.get('back_color')
        
        qr = qrcode.QRCode(
            version=3,
            border=2,
            box_size=10
        )
        qr.add_data(url)
        qr_view = qr.make_image(fill_color= fill_color, back_color= back_color)
        qr_view.save(os.path.abspath(__file__ + "/../static/create_qrc/imgs/qrcode.png"))
    return render(request, "create_qrc/qrc.html", context= {"is_auth": True, 'username': request.user})