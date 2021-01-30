from django.shortcuts import render
from django.conf import settings

# Create your views here.
# Create your views here.
def home_view(request):
    return render(request,'hospital/dashboard.html')
def dash_view(request):
    return render(request,'hospital/dashboard.html')
def about_view(request):
    return render(request,'hospital/user.html')
def news_view(request):
    return render(request,'hospital/notifications.html')
def contact_us_view(request):
    return render(request,'hospital/icons.html')
def signup_view(request):
    return render(request,'hospital/tables.html')
def login_view(request):
    return render(request,'hospital/typography.html')