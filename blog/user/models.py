from django.db import models
from django.contrib.auth.models import User
from subscribes.models import Subscribe

# Create your models here.

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    subscribe = models.ForeignKey(Subscribe, on_delete= models.PROTECT, default=1)
    qrcodes_created = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username