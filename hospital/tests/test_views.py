from django.test import TestCase,Client
from django.urls import reverse
from hospital.models import Patient,Admin,Doctor,User,Appointment
from hospital.forms import AdminAppointmentForm
import json
from django.utils import timezone
from datetime import date,timedelta,time

class TestViews(TestCase):
    nu = User(username='username',email='email@gmail.com',password='password1')
    doc = Doctor(user=nu,firstname='firstname',
                        lastname='lastname',
                        department='department',
                        dob='12/12/12',
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    pat = Patient(user=nu,firstname='firstname',
                        lastname='lastname',
                        dob='12/12/12',
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    
    def test_GET_home_view(self):
        client = Client()
        response = client.get(reverse(''))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'hospital/Home/home.html')

    def test_GET_login_view(self):
        client = Client()
        response = client.get(reverse('login.html'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'hospital/Home/login.html')

    def test_GET_login_pat_view(self):
        client = Client()
        response = client.get(reverse('login_pat.html'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'hospital/Patient/login_pat.html')
    
    def test_GET_bookapp_adm_view(self):
        client = Client()
        #appointmentForm = AdminAppointmentForm()

        #response = client.get(reverse('bookapp_adm.html',args=[appointmentForm]))
        response = client.get(reverse('bookapp_adm.html'))
        self.assertEquals(response.status_code,302)
        #self.assertTemplateUsed(response,'hospital/Admin/bookapp_adm.html')
    
    def test_POST_bookapp_adm_view(self):
        client = Client()
        dt = timezone.now().date()
        tm = timezone.now().time()
        response = client.post(reverse('bookapp_adm.html'),{
            'description': "testing bookapp_adm",
            'calldate': dt,
            "calltime": tm,
            'doctor': self.doc,
            'patient': self.pat
        })
        self.assertEquals(response.status_code,302)
 