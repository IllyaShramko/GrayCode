from django.shortcuts import render
from .models import QRcodes
from user.models import Profile
from django.core.files.storage import FileSystemStorage
import qrcode, os
from PIL import Image
# Create your views here.

def render_create_qrc(request):
    if request.method == "POST":


        name = request.POST.get('name')
        url = request.POST.get('url')
        fill_color = request.POST.get('fill_color')
        back_color = request.POST.get('back_color')
        icon_in_center = request.FILES.get('icon_in_center')

        print(icon_in_center)

        QRcode= QRcodes.objects.create(
            name= name,
            qrcode_img = f"images/qrcodes/{name}.png",
            user= Profile.objects.get(user=request.user)
        )
        QRcode.save()
        
        qr = qrcode.QRCode(
            version=1,
            border=2,
            box_size=10
        )

        qr.add_data(url)
        qr_view = qr.make_image(fill_color= fill_color, back_color= back_color)
        if icon_in_center:
            image_path = os.path.join("images", "posts", icon_in_center.name)
            file_system = FileSystemStorage()
            file_system.save(image_path, icon_in_center)
              
            logo = Image.open(os.path.abspath(__file__ + f"/../../media/{image_path}"))

            qr_size = qr_view.size[0]
            logo_size = int(qr_size * 0.35)
            logo = logo.resize((logo_size, logo_size))

            pos = ((qr_view.size[0] - logo_size) // 2, (qr_view.size[1] - logo_size) // 2)
            qr_view.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

        qr_view.save(os.path.abspath(__file__ + "/../../media/images/qrcodes/qrcode.png"))
        qr_view.save(os.path.abspath(__file__ + f"/../../media/images/qrcodes/{name}.png"))
    print(QRcodes.objects.all()[0])
    return render(request, "create_qrc/qrc.html", context= {"is_auth": True, 'username': request.user, 'qrcode': QRcodes.objects.all()[0]})