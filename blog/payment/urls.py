from django.urls import path
from .views import *

urlpatterns = [
    path("standart/", render_payment_standart, name = "payment_standart"),
    path("pro/", render_payment_pro, name = "payment_pro")

]