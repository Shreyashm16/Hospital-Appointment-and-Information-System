from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.



departments=[('Cardiologist','Cardiologist'),
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Allergist/Immunologist','Allergist/Immunologist'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon')
]

def defaultuser():
    us = User(username="deleteduser",email="deleteduser@deleted.com")
    return us.id

class Doctor(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="Doctor")
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    firstname = models.CharField(max_length=100,default='firstname')
    lastname = models.CharField(max_length=100,default='lastname')
    age = models.IntegerField(default=0)
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.id}'
        


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Admin")
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
        return f'{self.user.username} Admin Profile'


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Patient")
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    firstname = models.CharField(max_length=100,default='firstname')
    lastname = models.CharField(max_length=100,default='lastname')
    age = models.IntegerField(default=0)
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    symptoms = models.CharField(max_length=100,default="fever")
    status=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} Patient Profile'



class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField()
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    #symptoms = models.CharField(max_length=100,default="fever")
    def __str__(self):
        return f'{self.patientName} Appointment Info'