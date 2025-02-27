"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from create_qrc.views import render_create_qrc
from django.contrib import admin
from django.urls import path, include
from home_app.views import render_home
from user.views import render_login
from user.views import render_registration
from subscribes.views import render_subs
from my_qrs.views import render_my_qrs, redirect_qrcode
from payment.views import  render_payment
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_qrc/', render_create_qrc, name= "generate"),
    path('', render_home, name = 'home'),
    path('user/', include("user.urls")),
    path('subscribes/', render_subs, name = 'subscribes'),
    path('view_qrcode/<int:pk>', redirect_qrcode, name= 'view_qrcode'),
    path('payment/<int:pk>', render_payment, name= 'payment'),
    path('my_qrs/', render_my_qrs, name="my_qrs")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)