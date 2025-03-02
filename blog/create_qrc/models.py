from django.db import models
from user.models import Profile
from subscribes.models import Subscribe
from django.urls import reverse
# Create your models here.
class QRcodes(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date = models.DateField(auto_now=True)
    qrcode_img = models.ImageField(upload_to='images/qrcodes')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subscribe_created = models.ForeignKey(Subscribe, on_delete=models.CASCADE, null=True)
    url = models.TextField(null=True)
    date_delete = models.DateTimeField(null=True)
    

    def get_absolute_url(self):
        return reverse('view_qrcode', kwargs= {'pk': self.pk})
    def __str__(self):
        return self.name