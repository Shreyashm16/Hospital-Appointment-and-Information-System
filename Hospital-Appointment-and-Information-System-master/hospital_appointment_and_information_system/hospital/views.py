from django.shortcuts import render
from django.conf import settings

# Create your views here.
# Create your views here.
def dash_view(request):
    return render(request,'hospital/dashboard.html')
def bookapp_view(request):
    return render(request,'hospital/bookapp.html')
def calladoc_view(request):
    return render(request,'hospital/calladoc.html')
def feedback_view(request):
    return render(request,'hospital/feedback.html')
def medicalreport_view(request):
    return render(request,'hospital/medicalreport.html')
def profile_view(request):
    return render(request,'hospital/profile.html')
def yourhealth_view(request):
    return render(request,'hospital/yourhealth.html')
def home_view(request):
    return render(request,'hospital/home.html')
def services_view(request):
    return render(request,'hospital/services.html')
def contactus_view(request):
    return render(request,'hospital/contactus.html')
def news_view(request):
    return render(request,'hospital/news.html')
def login_view(request):
    return render(request,'hospital/login.html')