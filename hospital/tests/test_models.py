from django.test import TestCase
from hospital.models import Patient,Admin,Doctor,User,Appointment,PatHealth
from django.utils import timezone

class AppointmentTest(TestCase):
    nu = User(username='username',email='email@gmail.com',password='password1')
    dt = timezone.now().date()
    doc = Doctor(user=nu,firstname='firstname',
                        lastname='lastname',
                        department='department',
                        dob=dt,
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    pat = Patient(user=nu,firstname='firstname',
                        lastname='lastname',
                        dob=dt,
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    
    def test_appcreation(self):
        dt = timezone.now().date()
        tm = timezone.now().time()
        self.nu.save()
        self.doc.save()
        self.pat.save()
        app = Appointment.objects.create(doctor=self.doc,patient=self.pat,calldate=dt,calltime=tm,description="testing appointment creation")
        self.assertEquals(str(app),"testing appointment creation Appointment Info")

    def test_pathealthcreation(self):
        self.nu.save()
        self.pat.save()
        ph = PatHealth(patient=self.pat,height=170,weight=70,diseases="test disease",medicines="test medicines", ts="test treatment/surgery")
        self.assertEquals(str(ph),"username Patient Profile Health Info")