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
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
<<<<<<< HEAD

    department= forms.MultipleChoiceField(choices=dep)
    department.widget.attrs.update({'class' : 'app-form-control'})
=======
>>>>>>> 06f3f2813e36ea63e4a7302e7756a96a81879ddc
    
    age = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'AGE'}))
    age.widget.attrs.update({'class' : 'app-form-control'})
    
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'POSTAL CODE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    image = forms.ImageField(label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    image.widget.attrs.update({'class' : 'app-form-control'})
    
<<<<<<< HEAD
    
=======
    department = forms.CharField(label="",widget = forms.Select(choices=dep))
    department.widget.attrs.update({'class' : 'app-form-control'})

>>>>>>> 06f3f2813e36ea63e4a7302e7756a96a81879ddc
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

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
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    age = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'AGE'}))
    age.widget.attrs.update({'class' : 'app-form-control'})
    
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'POSTAL CODE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    image = forms.ImageField(label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

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
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    age = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'AGE'}))
    age.widget.attrs.update({'class' : 'app-form-control'})
    
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'POSTAL CODE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    image = forms.ImageField(label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    symptoms = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'SYMPTOMS'}))
    symptoms.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

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
    #doctorId=forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    doctorId=forms.IntegerField()
    description = forms.CharField()
    appointmentDate = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    class Meta:
        model=Appointment
        fields=['doctorId','description','appointmentDate']