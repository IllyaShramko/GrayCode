from django.shortcuts import render, redirect
from user.models import Profile
# Create your views here.
from django.contrib.auth.decorators import login_required
from subscribes.models import Subscribe
@login_required

def render_subs(request):
    profiles = Profile.objects.filter(user_id= request.user.id)
    subscribes = Subscribe.objects.all()
    profile = profiles[0]
    if request.method == "POST":
        switch_subscribe = request.POST.get('button')
        print(switch_subscribe)
        if switch_subscribe == "base":
            profile.subscribe_id = 1
        elif switch_subscribe == "standart":
            return redirect(subscribes[1].get_absolute_url())
        elif switch_subscribe == "pro":
            return redirect(subscribes[2].get_absolute_url())
        elif switch_subscribe == "universal":
            return redirect(subscribes[3].get_absolute_url())
        profile.save()
    
    return render(request, "subscribes/subs.html", context={"is_auth": True, "username": request.user, "type_sub": profile.subscribe.name})
