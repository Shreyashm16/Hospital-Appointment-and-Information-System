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
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username}'
        


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Admin")
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    firstname = models.CharField(max_length=100,default='firstname')
    lastname = models.CharField(max_length=100,default='lastname')
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
    dob = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=300,default="address")
    city = models.CharField(max_length=100,default="city")
    country = models.CharField(max_length=100,default="country")
    postalcode = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} Patient Profile'



class Appointment(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientApp")
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="DoctorApp")
    description=models.TextField(max_length=500)
    link=models.TextField(null=True)
    calldate=models.DateField(null=True)
    calltime=models.TimeField(null=True)
    status=models.BooleanField(default=False)
    finished=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.description} Appointment Info'


class PatHealth(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientHealth")
    height=models.FloatField(default=0)
    weight=models.FloatField(default=0)
    diseases=models.CharField(max_length=2000,default='somediseases')
    medicines=models.CharField(max_length=2000,default='somemedicines')
    ts=models.CharField(max_length=2000,default='treatments/surgery')
    status=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.patient} Health Info'


class PatAdmit(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientAdmit")
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="DoctorAdmit")
    admitDate=models.DateField()
    description=models.TextField()
    dischargeDate=models.DateField(null=True)
    #roomcharges=models.FloatField()
    def __str__(self):
        return f'{self.patient} Admit Info'

class Medicines(models.Model):
    name = models.TextField()
    price = models.FloatField()
    def __str__(self):
        return f'{self.name} Info'

class Charges(models.Model):
    Admitinfo=models.ForeignKey(PatAdmit, on_delete=models.CASCADE, related_name="AdmitDetails")
    commodity=models.ForeignKey(Medicines, on_delete=models.CASCADE, related_name="AdmitDetails")
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return f'{self.commodity} Info'


class DoctorProfessional(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="DoctorProfessional")
    appfees=models.FloatField()
    admfees=models.FloatField()
    totalpat = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.doctor.firstname} Professional Info'


class OperationCosts(models.Model):
    name=models.TextField()
    cost=models.FloatField()
    description=models.TextField(null=True)
    def __str__(self):
        return f'{self.name} Cost'
