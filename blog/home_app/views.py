from django.shortcuts import render
from subscribes.models import Subscribe
from user.models import Profile

# Create your views here.
def render_home(request):
    try:
        Subscribe.objects.create(
            name= "base",
            description= "1",
            cost_per_month= "0$"
        )
        print('123')
        Subscribe.objects.create(
            name= "standart",
            description= "1",
            cost_per_month= "2$"
        )
        print('123')
        Subscribe.objects.create(
            name= "pro",
            description= "1",
            cost_per_month= "10$"
        )
        print('123')
        Subscribe.objects.create(
            name= "universal",
            description= "1",
            cost_per_month= "15$"
        )
        print('123')
    except Exception as e:
        print(e)
    profiles = Profile.objects.filter(user_id= request.user.id)
    profile = profiles[0]
    return render(request, "home_app/home_app.html", context={"is_auth": request.user.is_authenticated, 'username': request.user, "type_sub": profile.subscribe.name})
