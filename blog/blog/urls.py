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
from user.views import render_login
from user.views import render_registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_qrc/', render_create_qrc),
    path('user/', include("user.urls")),
]
