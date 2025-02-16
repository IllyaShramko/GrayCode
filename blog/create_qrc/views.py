
from django.shortcuts import render
from .models import QRcodes
from user.models import Profile
from django.core.files.storage import FileSystemStorage
import qrcode, os
from PIL import Image
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, CircleModuleDrawer, SquareModuleDrawer,RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask

from PIL import ImageColor
# Create your views here.
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
modules_driwer = {
    "square": SquareModuleDrawer(),
    "gapped": GappedSquareModuleDrawer(),
    "circle": CircleModuleDrawer(),
    "rounded": RoundedModuleDrawer(),
    "vertical": VerticalBarsDrawer(),
    "horizontal": HorizontalBarsDrawer()
}
def render_create_qrc(request):
    try:
        os.mkdir(os.path.abspath(__file__ + f"/../../media/images/qrcodes"))
    except:
        print("Error Make Base Qrcodes Mkdir | 29")
    if request.method == "POST":
        name = request.POST.get('name')
        url = request.POST.get('url')
        fill_color_hex = request.POST.get('fill_color')
        back_color_hex = request.POST.get('back_color')
        icon_in_center = request.FILES.get('icon_in_center')
        size_qrcode = request.POST.get('size')
        module_driwer_type = request.POST.get('body')
        # 
        fill_color = hex_to_rgb(fill_color_hex)
        back_color = hex_to_rgb(back_color_hex)
        # 
        if size_qrcode == "256px":
            def_size_qrcode = 10
        elif size_qrcode == "512px":
            def_size_qrcode = 20
        elif size_qrcode == "1028px":
            def_size_qrcode = 30
        else:
            def_size_qrcode = 10

        QRcode= QRcodes.objects.create(
            name= name,
            qrcode_img = f"images/qrcodes/{request.user.username}/{name}.png",
            user= Profile.objects.get(user=request.user)
        )
        QRcode.save()

        qr = qrcode.QRCode(
            version=1,
            error_correction= qrcode.ERROR_CORRECT_H,
            border=2,
            box_size=def_size_qrcode
        )

        qr.add_data(url)
        qr.make(fit=True)

        if icon_in_center:
            image_path = os.path.join("images", "icons", icon_in_center.name)
            file_system = FileSystemStorage()
            file_system.save(image_path, icon_in_center)
            qr_view = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer= modules_driwer[module_driwer_type],
                embeded_image_path= os.path.abspath(__file__ + f"/../../media/{image_path}"),
                color_mask=SolidFillColorMask(front_color=fill_color, back_color=back_color)
            )
        else:
            print("1")
            qr_view = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer= modules_driwer[module_driwer_type],
                color_mask= SolidFillColorMask(front_color= fill_color, back_color=back_color)
            )


        print(qr_view)
        print(back_color)
        qr_view.save(os.path.abspath(__file__ + "/../static/create_qrc/images/qrcode.png"))
        try:
            os.mkdir(os.path.abspath(__file__ + f"/../../media/images/qrcodes/{request.user.username}"))
        except:
            print("Error Mkdir")
        qr_view.save(os.path.abspath(__file__ + f"/../../media/images/qrcodes/{request.user.username}/{name}.png"))
    
    profiles = Profile.objects.filter(user_id= request.user.id)
    profile = profiles[0]

    if profile.subscribe_id == 1:
        type_sub = "base"
    elif profile.subscribe_id == 2:
        type_sub = "standart"
    elif profile.subscribe_id == 3:
        type_sub = "pro"
    return render(request, "create_qrc/qrc.html", context= {"is_auth": True, 'username': request.user.username, 'type_sub': type_sub})