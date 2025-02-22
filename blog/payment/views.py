from django.shortcuts import render, redirect
from user.models import Profile
from subscribes.models import Subscribe
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def render_payment_standart(request):
    profiles = Profile.objects.filter(user_id= request.user.id)
    profile = profiles[0]
    type_switch_sub = "Standart"
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        number_card = request.POST.get("number-card")
        expire_date = request.POST.get("expire-date")
        security_code = request.POST.get("security-code")
        print(name, surname, number_card, expire_date, security_code)
        profile.subscribe_id = 2
        profile.save()
        return redirect("subscribes")
    return render(request, "payment/payment.html", context={"is_auth": True, "username": request.user, 'type_switch_sub': type_switch_sub})

@login_required
def render_payment_pro(request):
    profiles = Profile.objects.filter(user_id= request.user.id)
    profile = profiles[0]
    type_switch_sub = "Pro"
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        number_card = request.POST.get("number-card")
        expire_date = request.POST.get("expire-date")
        security_code = request.POST.get("security-code")
        print(name, surname, number_card, expire_date, security_code)
        profile.subscribe_id = 3
        profile.save()
        return redirect("subscribes")

    return render(request, "payment/payment.html", context={"is_auth": True, "username": request.user, 'type_switch_sub': type_switch_sub})