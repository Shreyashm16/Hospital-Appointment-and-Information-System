from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Doctor,Admin,Patient,Appointment
import datetime
from django.forms.widgets import SelectDateWidget

dep=[('Cardiologist','Cardiologist'),
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Allergist/Immunologist','Allergist/Immunologist'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon')
]

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    Name.widget.attrs.update({'class' : 'app-form-control'})
    Email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    Email.widget.attrs.update({'class' : 'app-form-control'})
    Message = forms.CharField(max_length=500,label="",widget=forms.TextInput(attrs={'placeholder': 'MESSAGE'}))
    Message.widget.attrs.update({'class' : 'app-form-control'})

class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField(initial="india")
    postalcode = forms.IntegerField()
    image = forms.ImageField()
    department= forms.MultipleChoiceField(choices=dep)
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname','department', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image', 'password1', 'password2']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class DoctorUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Doctor
        fields = ['firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField()
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image', 'password1', 'password2']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AdminUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Admin
        fields = ['firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class PatientRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField()
    symptoms = forms.CharField()
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'symptoms', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PatientUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    symptoms = forms.CharField()
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname','symptoms', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    description = forms.CharField()
    class Meta:
        model=Appointment
        fields=['description','status']