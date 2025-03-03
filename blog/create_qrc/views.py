from django.shortcuts import render, get_object_or_404
from .models import QRcodes
from user.models import Profile
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
import qrcode, os, time
from PIL import Image
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, CircleModuleDrawer, SquareModuleDrawer,RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask
from django.contrib.auth.decorators import login_required


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


@login_required
def render_create_qrc(request: HttpRequest):
    print(request.build_absolute_uri())
    list_absolute_url_default = request.build_absolute_uri().split("/")
    print(list_absolute_url_default)
    absolute_url = ""
    del list_absolute_url_default[-1]
    del list_absolute_url_default[-1]
    for element in list_absolute_url_default:
        absolute_url += element + '/'
    
    print(time.localtime())
    try:
        os.mkdir(os.path.abspath(__file__ + f"/../../media/"))
        os.mkdir(os.path.abspath(__file__ + f"/../../media/images/"))
        os.mkdir(os.path.abspath(__file__ + f"/../../media/images/qrcodes"))
    except:
        print("Error Make Base Qrcodes Mkdir | 29")
    current_profile = Profile.objects.get(user_id = request.user.id)
    generate_qrcode = False
    alert= False

    if current_profile.subscribe.name == "base":
        if current_profile.qrcodes_created < 1:
            generate_qrcode= True
    elif current_profile.subscribe.name == "standart":
        if current_profile.qrcodes_created < 10:
            generate_qrcode= True
    elif current_profile.subscribe.name == "pro":
        if current_profile.qrcodes_created < 50:
            generate_qrcode= True
    elif current_profile.subscribe.name == "universal":
        if current_profile.qrcodes_created < 125:
            generate_qrcode= True
    if request.method == "POST":
        if generate_qrcode:
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
            print(fill_color, back_color)
            # 
            print(fill_color, back_color)
            if size_qrcode == "256px":
                def_size_qrcode = 10
            elif size_qrcode == "512px":
                def_size_qrcode = 10
            elif size_qrcode == "1028px":
                def_size_qrcode = 20
            else:
                def_size_qrcode = 10

            date_delete = time.localtime()
            delete_year = date_delete.tm_year
            delete_month = date_delete.tm_mon
            delete_day = date_delete.tm_mday
            if delete_month < 7:
                date_delete = f"{delete_year}-{delete_month + 6}-{delete_day} {date_delete.tm_hour}:{date_delete.tm_min}"
            elif delete_month > 6:
                date_delete = f"{delete_year + 1}-{delete_month - 6}-{delete_day} {date_delete.tm_hour}:{date_delete.tm_min}"

            QRcode= QRcodes.objects.create(
                name= name,
                qrcode_img = f"images/qrcodes/{request.user.username}/{name}.png",
                user= Profile.objects.get(user=request.user),
                url = url,
                date_delete = date_delete,
                subscribe_created= Profile.objects.get(user=request.user).subscribe
            )
            QRcode.save()

            qr = qrcode.QRCode(
                version=1,
                error_correction= qrcode.ERROR_CORRECT_H,
                border=2,
                box_size=def_size_qrcode
            )
            if "https://" in url:
                qr.add_data(absolute_url + QRcode.get_absolute_url())
            else:
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
                    color_mask= SolidFillColorMask(front_color=fill_color, back_color=back_color)
                )
            else:
                print("1")
                qr_view = qr.make_image(
                    image_factory=StyledPilImage,
                    module_drawer= modules_driwer[module_driwer_type],
                    color_mask= SolidFillColorMask(front_color=fill_color, back_color=back_color)
                )
            
            print(qr_view)
            print(back_color)
            qr_view.save(os.path.abspath(__file__ + "/../static/create_qrc/images/qrcode.png"))
            try:
                os.mkdir(os.path.abspath(__file__ + f"/../../media/images/qrcodes/{request.user.username}"))
            except:
                print("Error Mkdir")
            qr_view.save(os.path.abspath(__file__ + f"/../../media/images/qrcodes/{request.user.username}/{name}.png"))
            current_profile.qrcodes_created += 1
            current_profile.save()
        else:
            alert = True
    profiles = Profile.objects.filter(user_id= request.user.id)
    profile = profiles[0]

    return render(request, "create_qrc/qrc.html", context= {"is_auth": True, 'username': request.user.username, 'type_sub': profile.subscribe.name, "alert": alert})

# def redirect_user_to_qrcode_url():
