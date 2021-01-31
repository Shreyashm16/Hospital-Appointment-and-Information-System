from django.shortcuts import render
from django.conf import settings

# Create your views here.
# Create your views here.
def dash_view(request):
    return render(request,'hospital/Patient/dashboard.html')
def bookapp_view(request):
    return render(request,'hospital/Patient/bookapp.html')
def calladoc_view(request):
    return render(request,'hospital/Patient/calladoc.html')
def feedback_view(request):
    return render(request,'hospital/Patient/feedback.html')
def medicalreport_view(request):
    return render(request,'hospital/Patient/medicalreport.html')
def profile_view(request):
    return render(request,'hospital/Patient/profile.html')
def yourhealth_view(request):
    return render(request,'hospital/Patient/yourhealth.html')
def dash_doc_view(request):
    return render(request,'hospital/Doctor/dashboard_doc.html')
def bookapp_doc_view(request):
    return render(request,'hospital/Doctor/bookapp_doc.html')
def calladoc_doc_view(request):
    return render(request,'hospital/Doctor/calladoc_doc.html')
def feedback_doc_view(request):
    return render(request,'hospital/Doctor/feedback_doc.html')
def medicalreport_doc_view(request):
    return render(request,'hospital/Doctor/medicalreport_doc.html')
def profile_doc_view(request):
    return render(request,'hospital/Doctor/profile_doc.html')
def yourhealth_doc_view(request):
    return render(request,'hospital/Doctor/yourhealth_doc.html')
def home_view(request):
    return render(request,'hospital/Home/home.html')
#def services_view(request):
#    return render(request,'hospital/Home/services.html')
#def contactus_view(request):
#    return render(request,'hospital/Home/contactus.html')
#def news_view(request):
#    return render(request,'hospital/Home/news.html')
def login_view(request):
    return render(request,'hospital/Home/login.html')