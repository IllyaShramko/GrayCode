from django.urls import path
from .views import *

urlpatterns = [
    path('my_qrs/', render_my_qrs, name = 'my_qrs'),
]