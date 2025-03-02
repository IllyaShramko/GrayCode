from django.db import models
from django.urls import reverse
# from user.models import Profile
# Create your models here.
class Subscribe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    cost_per_month = models.CharField(max_length=255)
    
    def get_absolute_url(self):
        return reverse('payment', kwargs= {'pk': self.pk})
    def __str__(self):
        return self.name