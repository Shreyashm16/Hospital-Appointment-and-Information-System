from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import pat_Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image', 'password1', 'password2']

    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    #image = forms.ImageField()

    class Meta:
        model = User
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']
        fields = ['username','email']


class pat_ProfileUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = pat_Profile
        fields = ['firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']