from django.shortcuts import render, redirect
from user.models import Profile
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required

def render_subs(request):
    profiles = Profile.objects.filter(user_id= request.user.id)
    profile = profiles[0]
    if request.method == "POST":
        switch_subscribe = request.POST.get('button')
        print(switch_subscribe)
        if switch_subscribe == "base":
            profile.subscribe_id = 1
        elif switch_subscribe == "standart":
            return redirect("payment_standart")
        elif switch_subscribe == "pro":
            return redirect("payment_pro")
        profile.save()
    
    if profile.subscribe_id == 1:
        type_sub = "base"
    elif profile.subscribe_id == 2:
        type_sub = "standart"
    elif profile.subscribe_id == 3:
        type_sub = "pro"
    return render(request, "subscribes/subs.html", context={"is_auth": True, "username": request.user, "type_sub": type_sub})
