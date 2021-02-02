from django.shortcuts import render
from django.conf import settings

# Create your views here.
# Create your views here.
def home_view(request):
    return render(request,'hospital/index.html')
def about_view(request):
    return render(request,'hospital/about.html')
def news_view(request):
    return render(request,'hospital/news.html')
def contact_us_view(request):
    return render(request,'hospital/contact_us.html')
def signup_view(request):
    return render(request,'hospital/signup.html')
def login_view(request):
    return render(request,'hospital/login.html')