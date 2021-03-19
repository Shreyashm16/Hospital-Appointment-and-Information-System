from django import forms
from django.contrib.auth.models import User
from . import models


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    Name.widget.attrs.update({'class' : 'app-form-control'})
    Email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    Email.widget.attrs.update({'class' : 'app-form-control'})
    Message = forms.CharField(max_length=500,label="",widget=forms.TextInput(attrs={'placeholder': 'MESSAGE'}))
    Message.widget.attrs.update({'class' : 'app-form-control'})


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    #----#
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic']