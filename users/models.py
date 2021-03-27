from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class pat_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pat_Profile")
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    firstname = models.CharField(max_length=100,default='firstname')
    lastname = models.CharField(max_length=100,default='lastname')
    age = models.IntegerField(default=0)
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user.username} Profile'