
from django.shortcuts import render
from .models import QRcodes
from user.models import Profile
from django.core.files.storage import FileSystemStorage
import qrcode, os
from PIL import Image
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, CircleModuleDrawer, SquareModuleDrawer,RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.image.styledpil import StyledPilImage

# Create your views here.

def render_create_qrc(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        url = request.POST.get('url')
        fill_color = request.POST.get('fill_color')
        back_color = request.POST.get('back_color')
        icon_in_center = request.FILES.get('icon_in_center')
        size_qrcode = request.POST.get('size')
        module_driwer_type = request.POST.get('body')
        
        if module_driwer_type == "square":
            module_driwer = SquareModuleDrawer()
        elif module_driwer_type == "gapped":
            module_driwer = GappedSquareModuleDrawer()
        elif module_driwer_type == "circle":
            module_driwer = CircleModuleDrawer()
        elif module_driwer_type == "rounded":
            module_driwer = RoundedModuleDrawer()
        elif module_driwer_type == "vertical":
            module_driwer = VerticalBarsDrawer()
        elif module_driwer_type == "horizontal":
            module_driwer = HorizontalBarsDrawer()
        
        if size_qrcode == "256px":
            def_size_qrcode = 20
        elif size_qrcode == "512px":
            def_size_qrcode = 30
        elif size_qrcode == "1028px":
            def_size_qrcode = 40
        else:
            def_size_qrcode = 10

        QRcode= QRcodes.objects.create(
            name= name,
            qrcode_img = f"images/qrcodes/{request.user.username}/{name}.png",
            user= Profile.objects.get(user=request.user)
        )
        QRcode.save()

        qr = qrcode.QRCode(
            version=2,
            error_correction= qrcode.ERROR_CORRECT_H,
            border=2,
            box_size=def_size_qrcode
        )

        qr.add_data(url)

        if icon_in_center:
            image_path = os.path.join("images", "icons", icon_in_center.name)
            file_system = FileSystemStorage()
            file_system.save(image_path, icon_in_center)
            qr_view = qr.make_image(
                module_drawer= module_driwer,
                image_factory=StyledPilImage,
                embeded_image_path= os.path.abspath(__file__ + f"/../../media/{image_path}"),
                fill_color= fill_color,
                back_color= back_color,
            )
        else:
            qr_view = qr.make_image(
                module_drawer= module_driwer,
                image_factory=StyledPilImage,
                fill_color= fill_color,
                back_color= back_color,
            )
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