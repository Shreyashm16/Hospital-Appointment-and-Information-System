from django.shortcuts import render,redirect,reverse
from django.conf import settings
from . import forms,models
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from .forms import DoctorRegisterForm,DoctorUpdateForm, AdminRegisterForm,AdminUpdateForm, PatientRegisterForm,PatientUpdateForm,PatientAppointmentForm,AdminAppointmentForm,YourHealthEditForm,PatAdmitEditForm
from django.contrib.auth.forms import AuthenticationForm
from hospital.models import Doctor,Admin,Patient,Appointment,User,PatHealth,PatAdmit
from django.contrib import auth
from django.utils import timezone
from datetime import date
from django.http import HttpResponseRedirect

## For Invoice Function
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

#Admin Related Views

@login_required(login_url='login_adm.html')
def bookapp_adm_view(request):
    if check_admin(request.user):
        if request.method=="POST":
            appointmentForm = AdminAppointmentForm(request.POST)
            if appointmentForm.is_valid():
                docid=appointmentForm.cleaned_data.get('doctor')
                patid=appointmentForm.cleaned_data.get('patient')
                doc = Doctor.objects.all().filter(id=docid).first()
                pat = Patient.objects.all().filter(id=patid).first()
                app = Appointment(patient=pat,doctor=doc,
                                    description=appointmentForm.cleaned_data.get('description'),
                                    appointmentDate=appointmentForm.cleaned_data.get('appointmentDate'),
                                    status=True)
                app.save()
                return redirect('bookapp_adm.html')
            else:
                print(appointmentForm.errors)
        else:
            appointmentForm = AdminAppointmentForm()
        return render(request,'hospital/Admin/bookapp_adm.html',{'appointmentForm': appointmentForm})
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def admin_appointment_view(request):
    if check_admin(request.user):
        det=[]
        for c in Appointment.objects.filter(status=True).all():
            d=c.doctor
            p=c.patient
            if d and p:
                det.append([d.firstname,p.firstname,c.description,c.appointmentDate])
        return render(request,'hospital/Admin/appoint_view_adm.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def dash_adm_view(request):
    if check_admin(request.user):
        doc = Doctor.objects.all().filter(status=False)
        pat = Patient.objects.all().filter(status=False)
        pattotcount=Patient.objects.all().count()
        doctotcount=Doctor.objects.all().count()
        appcount=Appointment.objects.all().count()
        patapp = Patient.objects.all().filter(status=False).count()
        docapp = Doctor.objects.all().filter(status=False).count()
        approveapp = Appointment.objects.all().filter(status=False).count()
        dic={'doc':doc,'pat':pat,'pattotcount':pattotcount,'doctotcount':doctotcount,'patapp':patapp,'docapp':docapp,'appcount':appcount,'approveapp':approveapp}
        return render(request,'hospital/Admin/dashboard_adm.html',context=dic)
    else:
        auth.logout(request)
        return redirect('login_adm.html')

def calladoc_adm_view(request):
    return render(request,'hospital/Admin/calladoc_adm.html')
def medicalreport_adm_view(request):
    return render(request,'hospital/Admin/medicalreport_adm.html')
def yourhealth_adm_view(request):
    return render(request,'hospital/Admin/yourhealth_adm.html')


def login_adm_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and check_admin(user):
                auth.login(request, user)
                return redirect('dashboard_adm.html')
        return render(request, 'hospital/Admin/login_adm.html', {'form': form})
    else: 
        form = AuthenticationForm()
                
    return render(request, 'hospital/Admin/login_adm.html', {'form': form})

def register_adm_view(request):
    if request.method=="POST":
        form = AdminRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))
            adm = Admin(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        age=form.cleaned_data.get('age'),
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image']
                        )
            adm.save()
            mpg = Group.objects.get_or_create(name='ADMIN')
            mpg[0].user_set.add(nu)
            return redirect('login_adm.html')
        else:
            print(form.errors)
    else: 
        form = AdminRegisterForm()
    
    return render(request,'hospital/Admin/register_adm.html',{'form': form})

@login_required(login_url='login_adm.html')
def patient_adm_view(request):
    if check_admin(request.user):
        pat = Patient.objects.all().filter(status=False)
        patapp = Patient.objects.all().filter(status=False).count()
        patcount=Patient.objects.all().count()
        dic={'pat':pat,'patcount':patcount,'patapp':patapp}
        return render(request,'hospital/Admin/patient_adm.html',context=dic)
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def doctor_adm_view(request):
    if check_admin(request.user):
        doc = Doctor.objects.all().filter(status=False)
        doccount=Doctor.objects.all().count()
        dic={'doc':doc,'doccount':doccount}
        return render(request,'hospital/Admin/doctor_adm.html',context=dic)
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def approve_pat_view(request):
    if check_admin(request.user):
        pat = Patient.objects.all().filter(status=False)
        return render(request,'hospital/Admin/approve_pat.html',{'pat':pat})
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def approve_doc_view(request):
    if check_admin(request.user):
        doc = Doctor.objects.all().filter(status=False)
        return render(request,'hospital/Admin/approve_doc.html',{'doc':doc})
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def approve_patient_view(request,pk):
    if check_admin(request.user):
        patient=Patient.objects.get(id=pk)
        patient.status=True
        patient.save()
        return redirect(reverse('approve_pat.html'))
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def approve_doctor_view(request,pk):
    if check_admin(request.user):
        doctor=Doctor.objects.get(id=pk)
        doctor.status=True
        doctor.save()
        return redirect(reverse('approve_doc.html'))
    else:
        auth.logout(request)
        return redirect('login_adm.html')


@login_required(login_url='login_adm.html')
def approve_appoint_view(request):
    if check_admin(request.user):
        #those whose approval are needed
        det=[]
        for c in Appointment.objects.filter(status=False).all():
            d=c.doctor
            p=c.patient
            if d and p:
                det.append([d.firstname,p.firstname,c.description,c.appointmentDate,c.id])
        return render(request,'hospital/Admin/approve_appoint.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def approve_app_view(request,pk):
    if check_admin(request.user):
        appointment=Appointment.objects.get(id=pk)
        appointment.status=True
        appointment.save()
        return redirect(reverse('approve_appoint.html'))
    else:
        auth.logout(request)
        return redirect('login_adm.html')

@login_required(login_url='login_adm.html')
def profile_adm_view(request):
    if check_admin(request.user):
        adm = Admin.objects.filter(user_id=request.user.id).first()
        #return render(request,'hospital/Doctor/profile_doc.html',{'doc':doc})
        if request.method=="POST":
            p_form = AdminUpdateForm(request.POST, request.FILES, instance=adm)
            if p_form.is_valid():
                p_form.save()
                return redirect('profile_adm.html')
        else:
            p_form = AdminUpdateForm(instance=adm)
        context = {
            'p_form': p_form,
            'adm': adm
        }
        return render(request,'hospital/Admin/profile_adm.html',context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')




# Paitent Related Views


@login_required(login_url='login_pat.html')
def dash_view(request):
    if check_patient(request.user):
        pat=Patient.objects.get(user_id=request.user.id)
        det=[]
        for c in Appointment.objects.filter(status=False,patient=pat).all():
            d=c.doctor
            # p=Patient.objects.filter(id=c.patientId).first()
            if d:
                det.append([d.firstname,c.description,d.department,c.appointmentDate])
        
        admt=[]
        for c in PatAdmit.objects.filter(patient=pat).all():
            d=c.doctor
            if d:
                admt.append([d.firstname,pat.firstname,c.admitDate,c.dischargeDate,c.pk])
        return render(request,'hospital/Patient/dashboard.html',{'app':det,'admt':admt})
    else:
        auth.logout(request)
        return redirect('login_pat.html')



@login_required(login_url='login_pat.html')
def bookapp_view(request):
    if check_patient(request.user):
        pat = Patient.objects.filter(user_id=request.user.id).first()
        if request.method=="POST":
            appointmentForm = PatientAppointmentForm(request.POST)
            if appointmentForm.is_valid():
                docid=int(appointmentForm.cleaned_data.get('doctor'))
                doc = Doctor.objects.all().filter(id=docid).first()
                app = Appointment(patient=pat,doctor=doc,
                                    description=appointmentForm.cleaned_data.get('description'),
                                    appointmentDate=appointmentForm.cleaned_data.get('appointmentDate'),
                                    status=False)
                app.save()
                return redirect('bookapp.html')
            else:
                print(appointmentForm.errors)
        else:
            appointmentForm = PatientAppointmentForm()
        return render(request,'hospital/Patient/bookapp.html',{'appointmentForm': appointmentForm})
    else:
        auth.logout(request)
        return redirect('login_pat.html')

@login_required(login_url='login_pat.html')
def pat_appointment_view(request):
    if check_patient(request.user):
        pat=Patient.objects.get(user_id=request.user.id)
        det=[]
        for c in Appointment.objects.filter(status=True,patient=pat).all():
            d=c.doctor
            p=c.patient
            if d and p:
                det.append([d.firstname,p.firstname,c.description,c.appointmentDate,c.link,c.calldate,c.calltime])
        return render(request,'hospital/Patient/appoint_view_pat.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_pat.html')

@login_required(login_url='login_pat.html')
def calladoc_view(request):
    if check_patient(request.user):
        pat=Patient.objects.get(user_id=request.user.id)
        det=[]
        for c in Appointment.objects.filter(status=True,patient=pat).all():
            d=c.doctor
            if d:
                det.append([d.firstname,pat.firstname,c.calldate,c.calltime,c.link])
        return render(request,'hospital/Patient/calladoc.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_pat.html')


@login_required(login_url='login_pat.html')
def feedback_view(request):
    if check_patient(request.user):
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
    else:
        auth.logout(request)
        return redirect('login_pat.html')

@login_required(login_url='login_pat.html')
def medicalreport_view(request):
    if check_patient(request.user):
        return render(request,'hospital/Patient/medicalreport.html')
    else:
        auth.logout(request)
        return redirect('login_pat.html')

@login_required(login_url='login_pat.html')
def admit_details_view(request):
    if check_patient(request.user):
        pat=Patient.objects.get(user_id=request.user.id)
        det=[]
        for c in PatAdmit.objects.filter(patient=pat).all():
            d=c.doctor
            if d:
                det.append([d.firstname,pat.firstname,c.admitDate,c.dischargeDate,c.pk])
        return render(request,'hospital/Patient/admit_details.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_pat.html')

@login_required(login_url='login_pat.html')
def admit_details_particular_view(request,pk):
    if check_patient(request.user):
        ad = PatAdmit.objects.filter(id=pk).first()
        pat=ad.patient
        doc=ad.doctor
        det=[doc.firstname,pat.firstname,ad.admitDate,ad.dischargeDate,ad.description]
        return render(request,'hospital/Patient/admit_details_particular.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_pat.html')

def login_pat_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and check_patient(user):
                auth.login(request, user)
                accountapproval=Patient.objects.all().filter(status=True,user_id=request.user.id)
                if accountapproval:
                    return redirect('profile_pat.html')
                else:
                    return render(request,'hospital/Home/wait_approval.html')
        return render(request, 'hospital/Patient/login_pat.html', {'form': form})
    else: 
        form = AuthenticationForm()
                
    return render(request, 'hospital/Patient/login_pat.html', {'form': form})

def register_pat_view(request):
    if request.method=="POST":
        form = PatientRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))
            p = Patient(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        age=form.cleaned_data.get('age'),
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image']
                        )
            p.save()
            path = PatHealth(patient=p,status=False)
            path.save()
            mpg = Group.objects.get_or_create(name='PATIENT')
            mpg[0].user_set.add(nu)
            return redirect('login_pat.html')
        else:
            print(form.errors)
    else: 
        form = PatientRegisterForm()
    
    return render(request,'hospital/Patient/register_pat.html',{'form': form})

@login_required(login_url='login_pat.html')
def profile_pat_view(request):
    if check_patient(request.user):
        pat = Patient.objects.filter(user_id=request.user.id).first()
        #return render(request,'hospital/Doctor/profile_doc.html',{'doc':doc})
        if request.method=="POST":
            p_form = PatientUpdateForm(request.POST, request.FILES, instance=pat)
            if p_form.is_valid():
                p_form.save()
                return redirect('profile_pat.html')
        else:
            p_form = PatientUpdateForm(instance=pat)
        context = {
            'p_form': p_form,
            'pat': pat
        }
        return render(request,'hospital/Patient/profile_pat.html',context)
    else:
        auth.logout(request)
        return redirect('login_pat.html')

@login_required(login_url='login_pat.html')
def yourhealth_view(request):
    if check_patient(request.user):
        pat = Patient.objects.filter(user_id=request.user.id).first()
        info=PatHealth.objects.filter(patient=pat).first()
        if info.status:
            return render(request,'hospital/Patient/yourhealth.html',{'info':info,'pat':pat})
        else:
            return redirect('edityourhealth.html')
    else:
        auth.logout(request)
        return redirect('login_pat.html')


@login_required(login_url='login_pat.html')
def edityourhealth_view(request):
    if check_patient(request.user):
        pat = Patient.objects.filter(user_id=request.user.id).first()
        info = PatHealth.objects.filter(patient=pat).first()
        if request.method=="POST":
            p_form = YourHealthEditForm(request.POST, instance=pat)
            if p_form.is_valid():
                info.height=p_form.cleaned_data.get('height')
                info.weight=p_form.cleaned_data.get('weight')
                info.diseases=p_form.cleaned_data.get('diseases')
                info.medicines=p_form.cleaned_data.get('medicines')
                info.ts=p_form.cleaned_data.get('ts')
                info.status=True
                info.save()
                p_form.save()
                return render(request,'hospital/Patient/yourhealth.html',{'info':info,'pat':pat})
        else:
            info.refresh_from_db()
            p_form = YourHealthEditForm(instance=pat)
            p_form.fields['height'].initial = info.height
            p_form.fields['weight'].initial = info.weight
            p_form.fields['diseases'].initial = info.diseases
            p_form.fields['medicines'].initial = info.medicines
            p_form.fields['ts'].initial = info.ts
            context = {
                'p_form': p_form,
                'info':info,
                'pat':pat
            }
            return render(request,'hospital/Patient/edityourhealth.html',context)
    else:
        auth.logout(request)
        return redirect('login_pat.html')




# Doctor Related Views

@login_required(login_url='login_doc.html')
def dash_doc_view(request):
    if check_doctor(request.user):
        doc=Doctor.objects.get(user_id=request.user.id)
        patcount=models.Appointment.objects.all().filter(status=True,doctor=request.user.id).count()
        appcount=models.Appointment.objects.all().filter(status=True,doctor=request.user.id).count()
        det=[]
        for c in Appointment.objects.filter(status=False,doctor=doc).all():
            p=c.patient
            if p:
                det.append([p.firstname,c.description,c.appointmentDate,c.link,c.id])
        
        admt=[]
        for c in PatAdmit.objects.filter(doctor=doc).all():
            p=c.patient
            if p:
                admt.append([doc.firstname,p.firstname,c.admitDate,c.dischargeDate,c.pk])
        return render(request,'hospital/Doctor/dashboard_doc.html',{'app':det,'patcount':patcount,'appcount':appcount,'admt':admt})
    else:
        auth.logout(request)
        return redirect('login_doc.html')

@login_required(login_url='login_doc.html')
def dash_doc_approve_view(request,pk):
    if check_doctor(request.user):
        appointment=Appointment.objects.get(id=pk)
        appointment.status=True
        appointment.save()
        return redirect(reverse('dashboard_doc.html'))
    else:
        auth.logout(request)
        return redirect('login_doc.html')

@login_required(login_url='login_doc.html')
def bookapp_doc_view(request):
    if check_doctor(request.user):
        doc=Doctor.objects.get(user_id=request.user.id)
        det=[]
        for c in Appointment.objects.filter(status=True,doctor=doc.id,link__isnull=True).all():
            p=Patient.objects.filter(id=c.patient.id).first()
            if p:
                det.append([p.firstname,c.description,c.appointmentDate,c.pk])
        if request.method=="POST":
            p_form = PatientAppointmentForm(request.POST, request.FILES, instance=doc)
            if p_form.is_valid():
                p_form.save()
                return redirect('profile_doc.html')
        return render(request,'hospital/Doctor/bookapp_doc.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_doc.html')

@login_required(login_url='login_doc.html')
def bookapp_doc_link_view(request,pk,date,time,link):
    if check_doctor(request.user):
        appointment=Appointment.objects.get(id=pk)
        appointment.calldate=date
        appointment.calltime=time
        appointment.link=link
        appointment.save()
        return redirect(reverse('bookapp_doc.html'))
    else:
        auth.logout(request)
        return redirect('login_doc.html')

@login_required(login_url='login_doc.html')
def feedback_doc_view(request):
    if check_doctor(request.user):
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
    else:
        auth.logout(request)
        return redirect('login_doc.html')
    
def login_doc_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and check_doctor(user):
                auth.login(request, user)
                accountapproval=Doctor.objects.all().filter(status=True,user_id=request.user.id)
                if accountapproval:
                    return redirect('profile_doc.html')
                else:
                    return render(request,'hospital/Home/wait_approval.html')
        return render(request, 'hospital/Doctor/login_doc.html', {'form': form})
    else: 
        form = AuthenticationForm()
                
    return render(request, 'hospital/Doctor/login_doc.html', {'form': form})

def register_doc_view(request):
    if request.method=="POST":
        form = DoctorRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            db = form.cleaned_data.get('dob')
            today = date.today()
            ag =  today.year - db.year - ((today.month, today.day) < (db.month, db.day))
            if db < timezone.now().date():
                nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))
                doc = Doctor(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        department=form.cleaned_data.get('department'),
                        age=ag,
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image']
                        )
                doc.save()
                mpg = Group.objects.get_or_create(name='DOCTOR')
                mpg[0].user_set.add(nu)
                return redirect('login_doc.html')
            else:
                form.add_error('dob', 'Invalid date of birth.')
                return render(request,'hospital/Doctor/register_doc.html',{'form': form})
        else:
            print(form.errors)
    else: 
        form = DoctorRegisterForm()
    
    return render(request,'hospital/Doctor/register_doc.html',{'form': form})



@login_required(login_url='login_doc.html')
def profile_doc_view(request):
    if check_doctor(request.user):
        doc = Doctor.objects.filter(user_id=request.user.id).first()
        #return render(request,'hospital/Doctor/profile_doc.html',{'doc':doc})
        if request.method=="POST":
            p_form = DoctorUpdateForm(request.POST, request.FILES, instance=doc)
            if p_form.is_valid():
                p_form.save()
                return redirect('profile_doc.html')
        else:
            p_form = DoctorUpdateForm(instance=doc)
        context = {
            'p_form': p_form,
            'doc': doc
        }
        return render(request,'hospital/Doctor/profile_doc.html',context)
    else:
        auth.logout(request)
        return redirect('login_doc.html')
    
@login_required(login_url='login_doc.html')
def yourhealth_doc_view(request):
    if check_doctor(request.user):
        return render(request,'hospital/Doctor/yourhealth_doc.html')
    else:
        auth.logout(request)
        return redirect('login_doc.html')

@login_required(login_url='login_doc.html')
def medicalreport_doc_view(request):
    if check_doctor(request.user):
        return render(request,'hospital/Doctor/medicalreport_doc.html')
    else:
        auth.logout(request)
        return redirect('login_doc.html')

@login_required(login_url='login_doc.html')
def admit_details_doc_view(request):
    if check_doctor(request.user):
        doc=Doctor.objects.get(user_id=request.user.id)
        det=[]
        for c in PatAdmit.objects.filter(doctor=doc).all():
            p=c.patient
            if p:
                det.append([doc.firstname,p.firstname,c.admitDate,c.dischargeDate,c.pk])
        return render(request,'hospital/Doctor/admit_details_doc.html',{'app':det})
    else:
        auth.logout(request)
        return redirect('login_doc.html')

@login_required(login_url='login_doc.html')
def admit_details_particular_doc_view(request,pk):
    if check_doctor(request.user):
        ad = PatAdmit.objects.filter(id=pk).first()
        pat=ad.patient
        doc=ad.doctor
        det=[doc.firstname,pat.firstname,ad.admitDate,ad.dischargeDate,ad.description]
        if request.method=="POST":
            p_form = PatAdmitEditForm(request.POST,instance=ad)
            if p_form.is_valid():
                ad.description=p_form.cleaned_data.get('description')
                ad.roomcharges=p_form.cleaned_data.get('roomcharges')
                ad.dischargeDate = p_form.cleaned_data.get('dischargeDate')
                ad.save()
                p_form.save()
                return redirect('admit_details_doc.html')
            else:
                print(p_form.errors)
        else:
            p_form = PatAdmitEditForm()
            return render(request,'hospital/Doctor/admit_details_particular_doc.html',{'app':det,'p_form':p_form})
    else:
        auth.logout(request)
        return redirect('login_doc.html')

# @login_required(login_url='login_doc.html')
# def doc_approve_appoint_view(request):
#     if check_doctor(request.user):
#         #those whose approval are needed from a particular Doctor
#         doc=Doctor.objects.get(user_id=request.user.id)
#         det=[]
#         for c in Appointment.objects.filter(status=False,doctorId=doc.id).all():
#             d=Doctor.objects.filter(id=c.doctorId).first()
#             p=Patient.objects.filter(id=c.patientId).first()
#             if d and p:
#                 det.append([p.firstname,c.description,c.appointmentDate,c.id])
#         return render(request,'hospital/Doctor/bookapp_doc.html',{'app':det})
#     else:
#         auth.logout(request)
#         return redirect('login_doc.html')

# @login_required(login_url='login_doc.html')
# def doc_approve_app_view(request,pk):
#     if check_doctor(request.user):
#         appointment=Appointment.objects.get(id=pk)
#         appointment.status=True
#         appointment.save()
#         return redirect(reverse('bookapp_doc.html'))
#     else:
#         auth.logout(request)
#         return redirect('login_doc.html')








def home_view(request):
    return render(request,'hospital/Home/home.html')


def login_view(request):
    return render(request,'hospital/Home/login.html')

@login_required(login_url='login_pat.html')
def bill_view(request):
    if check_doctor(request.user):
        pat = Patient.objects.filter(user_id=request.user.id).first()
        context = {
            'pat': pat
        }
        return render(request,'hospital/Patient/bill.html',context)
    else:
        auth.logout(request)
        return redirect('login_doc.html')
    



def check_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def check_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def check_patient(user):
    return user.groups.filter(name='PATIENT').exists()




def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return


## Discharge Details have not created yet

def download_pdf_view(request,pk):
    dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=pk).order_by('-id')[:1]
    dict={
        'patientName':dischargeDetails[0].patientName,
        'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
        'address':dischargeDetails[0].address,
        'symptoms':dischargeDetails[0].symptoms,
        'admitDate':dischargeDetails[0].admitDate,
        'releaseDate':dischargeDetails[0].releaseDate,
        'daySpent':dischargeDetails[0].daySpent,
        'medicineCost':dischargeDetails[0].medicineCost,
        'roomCharge':dischargeDetails[0].roomCharge,
        'doctorFee':dischargeDetails[0].doctorFee,
        'OtherCharge':dischargeDetails[0].OtherCharge,
        'total':dischargeDetails[0].total,
    }
    return render_to_pdf('hospital/download_bill.html',dict)




