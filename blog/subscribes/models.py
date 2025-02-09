from django.db import models
from user.models import Profile
# Create your models here.
class Subscribe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost_per_month = models.CharField(max_length=255)
    user = models.OneToOneField(Profile, on_delete= models.CASCADE)

    def __str__(self):
        return self.name