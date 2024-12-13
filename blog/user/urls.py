from django.urls import path
from .views import *

urlpatterns = [
    path("login/", render_login, name = "login"),
    path("registration/", render_registration, name = "registration")
]