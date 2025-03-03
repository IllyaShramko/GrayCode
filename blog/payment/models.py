# from django.db import models
# from user.models import Profile
# # Create your models here.
# class PaymentSubscriber(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     number_card = models.CharField(max_length=19)
#     expire_date = models.CharField(max_length=5)
#     cvv = models.CharField(max_length=3)

#     def __str__(self):
#         return self.name