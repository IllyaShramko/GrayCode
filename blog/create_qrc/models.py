from django.db import models
from user.models import Profile
# Create your models here.
class QRcodes(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date = models.DateField(auto_now=True)
    qrcode_img = models.ImageField(upload_to='images/qrcodes')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.TextField()
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name