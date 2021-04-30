from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Doctor,Admin,Patient,Appointment,PatHealth,PatAdmit
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

    # department= forms.MultipleChoiceField(choices=dep)
    # department.widget.attrs.update({'class' : 'app-form-control'})
    
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
    
    image = forms.ImageField(label="")
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    
    department = forms.CharField(label="",widget = forms.Select(choices=dep))
    department.widget.attrs.update({'class' : 'app-form-control'})

    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname','department', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
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
    
    image = forms.ImageField(label="")
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
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
    
    image = forms.ImageField(label="")
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
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
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class PatientAppointmentForm(forms.ModelForm):   
    #ch = [(c.pk, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]
    doctor = forms.TypedChoiceField()
    #doctorId=forms.CharField(widget=forms.Select(choices=c))  
    appointmentDate = forms.DateField(widget=SelectDateWidget(years=range(2021,2024)))

    def __init__(self, *args, **kwargs):
        super(PatientAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]
    
    class Meta:
        model=Appointment
        fields=['description']


class AdminAppointmentForm(forms.ModelForm):
    #patientId=forms.CharField(widget=forms.Select(choices=[(c.pk, c.firstname) for c in Patient.objects.all().filter(status=True)])) 
    #doctorId=forms.CharField(widget=forms.Select(choices=[(c.pk, c.firstname+"("+c.department+")") for c in Doctor.objects.all().filter(status=True)])) 
    doctor = forms.TypedChoiceField()
    patient = forms.TypedChoiceField()
    appointmentDate = forms.DateField(widget=SelectDateWidget(years=range(2021, 2024)))

    def __init__(self, *args, **kwargs):
        super(AdminAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]
        self.fields['patient'].choices = [(c.id, c.firstname) for c in Patient.objects.filter(status=True).all()]
    
    class Meta:
        model=Appointment
        fields=['description']



class YourHealthEditForm(forms.ModelForm):
    height = forms.FloatField()
    weight = forms.FloatField()
    diseases = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    medicines = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    ts  = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    class Meta:
        model = PatHealth
        fields = ['height','weight','diseases','medicines','ts']
    
        
class PatAdmitEditForm(forms.ModelForm):
    dischargeDate = forms.DateField(widget=SelectDateWidget(years=range(2021,2024)))
    roomcharges = forms.FloatField()
    description = forms.TextInput()
    class Meta:
        model = PatAdmit
        fields = ['dischargeDate','roomcharges','description']

