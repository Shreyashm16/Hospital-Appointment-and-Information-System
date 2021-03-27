from django.shortcuts import render,redirect,reverse
from django.conf import settings
from . import forms,models
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, pat_ProfileUpdateForm
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
def feedback_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/Home/home.html')
    return render(request, 'hospital/Patient/feedback.html', {'form':sub})
def medicalreport_view(request):
    return render(request,'hospital/Patient/medicalreport.html')
@login_required
def profile_view(request):
    if request.method=="POST":
        p_form = pat_ProfileUpdateForm(request.POST, request.FILES, instance=request.user.pat_Profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile.html')
    else:
        p_form = pat_ProfileUpdateForm(instance=request.user.pat_Profile)
    context = {
        'p_form': p_form
     }
    return render(request,'hospital/Patient/profile.html',context)
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
def feedback_doc_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/Home/home.html')
    return render(request, 'hospital/Doctor/feedback_doc.html', {'form':sub})

def medicalreport_doc_view(request):
    return render(request,'hospital/Doctor/medicalreport_doc.html')
def profile_doc_view(request):
    return render(request,'hospital/Doctor/profile_doc.html')
def yourhealth_doc_view(request):
    return render(request,'hospital/Doctor/yourhealth_doc.html')
def dash_adm_view(request):
    return render(request,'hospital/Admin/dashboard_adm.html')
def bookapp_adm_view(request):
    return render(request,'hospital/Admin/bookapp_adm.html')
def calladoc_adm_view(request):
    return render(request,'hospital/Admin/calladoc_adm.html')
def medicalreport_adm_view(request):
    return render(request,'hospital/Admin/medicalreport_adm.html')
def profile_adm_view(request):
    return render(request,'hospital/Admin/profile_adm.html')
def yourhealth_adm_view(request):
    return render(request,'hospital/Admin/yourhealth_adm.html')
def home_view(request):
    return render(request,'hospital/Home/home.html')
def signup_pat_view(request):
    return render(request,'hospital/Home/signup_pat.html')
def signup_doc_view(request):
    return render(request,'hospital/Home/signup_doc.html')
def signup_adm_view(request):
    return render(request,'hospital/Home/signup_adm.html')
#def services_view(request):
#    return render(request,'hospital/Home/services.html')
#def contactus_view(request):
#    return render(request,'hospital/Home/contactus.html')
#def news_view(request):
#    return render(request,'hospital/Home/news.html')
def login_view(request):
    return render(request,'hospital/Home/login.html')