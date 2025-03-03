from django.shortcuts import render, redirect
from user.models import Profile
from subscribes.models import Subscribe
# from .models import PaymentSubscriber
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def render_payment(request, pk):
    Subscribe_type = Subscribe.objects.get(pk=pk)
    profiles = Profile.objects.filter(user_id= request.user.id)
    profile = profiles[0]
    type_switch_sub = Subscribe_type.name
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        number_card = request.POST.get("number-card")
        expire_date = request.POST.get("expire-date")
        security_code = request.POST.get("security-code")

        print(name, surname, number_card, expire_date, security_code)
        profile.subscribe_id = pk
        profile.save()
        return redirect("subscribes")

    return render(request, "payment/payment.html", context={"is_auth": True, "username": request.user, 'type_switch_sub': type_switch_sub})
    