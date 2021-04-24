from django.shortcuts import render,redirect,reverse
from django.conf import settings
from . import forms,models
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from .forms import DoctorRegisterForm,DoctorUpdateForm, AdminRegisterForm,AdminUpdateForm, PatientRegisterForm,PatientUpdateForm,PatientAppointmentForm,AdminAppointmentForm
from django.contrib.auth.forms import AuthenticationForm
from hospital.models import Doctor,Admin,Patient,Appointment,User
from django.contrib import auth
from django.http import HttpResponseRedirect

## For Invoice Function
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

#Admin Related Views

@login_required
def bookapp_adm_view(request):
    if request.method=="POST":
        appointmentForm = AdminAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            docid=appointmentForm.cleaned_data.get('doctorId')
            patid=appointmentForm.cleaned_data.get('patientId')
            doc = Doctor.objects.all().filter(id=docid).first()
            pat = Patient.objects.all().filter(id=patid).first()
            app = Appointment(patientId=patid,doctorId=docid,
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

@login_required
def admin_appointment_view(request):
    det=[]
    for c in Appointment.objects.filter(status=True).all():
        d=Doctor.objects.filter(id=c.doctorId).first()
        p=Patient.objects.filter(id=c.patientId).first()
        if d and p:
            det.append([d.firstname,p.firstname,c.description,c.appointmentDate])
    return render(request,'hospital/Admin/appoint_view_adm.html',{'app':det})

@login_required
def dash_adm_view(request):
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

@login_required
def patient_adm_view(request):
    pat = Patient.objects.all().filter(status=False)
    patapp = Patient.objects.all().filter(status=False).count()
    patcount=Patient.objects.all().count()
    dic={'pat':pat,'patcount':patcount,'patapp':patapp}
    return render(request,'hospital/Admin/patient_adm.html',context=dic)

@login_required
def doctor_adm_view(request):
    doc = Doctor.objects.all().filter(status=False)
    doccount=Doctor.objects.all().count()
    dic={'doc':doc,'doccount':doccount}
    return render(request,'hospital/Admin/doctor_adm.html',context=dic)

@login_required
def approve_pat_view(request):
    pat = Patient.objects.all().filter(status=False)
    return render(request,'hospital/Admin/approve_pat.html',{'pat':pat})

@login_required
def approve_doc_view(request):
    doc = Doctor.objects.all().filter(status=False)
    return render(request,'hospital/Admin/approve_doc.html',{'doc':doc})

@login_required
def approve_patient_view(request,pk):
    patient=Patient.objects.get(id=pk)
    patient.status=True
    patient.save()
    return redirect(reverse('approve_pat.html'))

@login_required
def approve_doctor_view(request,pk):
    doctor=Doctor.objects.get(id=pk)
    doctor.status=True
    doctor.save()
    return redirect(reverse('approve_doc.html'))


@login_required
def approve_appoint_view(request):
    #those whose approval are needed
    det=[]
    for c in Appointment.objects.filter(status=False).all():
        d=Doctor.objects.filter(id=c.doctorId).first()
        p=Patient.objects.filter(id=c.patientId).first()
        if d and p:
            det.append([d.firstname,p.firstname,c.description,c.appointmentDate,c.id])
    return render(request,'hospital/Admin/approve_appoint.html',{'app':det})

@login_required
def approve_app_view(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('approve_appoint.html'))

@login_required
def profile_adm_view(request):
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




# Paitent Related Views

def dash_view(request):
    patient=Patient.objects.get(user_id=request.user.id)
    doctor=Doctor.objects.get(user_id=patient.assignedDoctorId)
    mydict={
    'patient':patient,
    'doctorName':doctor.firstname,
    'doctorpostal':doctor.postalcode,
    'doctorAddress':doctor.address,
    'symptoms':patient.symptoms,
    'doctorDepartment':doctor.department,
    'admitDate':patient.admitDate,
    }
    return render(request,'hospital/Patient/dashboard.html',context=mydict)

@login_required
def bookapp_view(request):
    pat = Patient.objects.filter(user_id=request.user.id).first()
    if request.method=="POST":
        appointmentForm = PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            docid=int(appointmentForm.cleaned_data.get('doctorId'))
            doc = Doctor.objects.all().filter(id=docid).first()
            app = Appointment(patientId=pat.id,doctorId=doc.id,
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

@login_required
def pat_appointment_view(request):
    pat=Patient.objects.get(user_id=request.user.id)
    det=[]
    for c in Appointment.objects.filter(status=True,patientId=pat.id).all():
        d=Doctor.objects.filter(id=c.doctorId).first()
        p=Patient.objects.filter(id=c.patientId).first()
        if d and p:
            det.append([d.firstname,p.firstname,c.description,c.appointmentDate])
    return render(request,'hospital/Patient/appoint_view_pat.html',{'app':det})


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
            doc = Patient(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        age=form.cleaned_data.get('age'),
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image'],
                        symptoms=form.cleaned_data.get('symptoms')
                        )
            doc.save()
            mpg = Group.objects.get_or_create(name='PATIENT')
            mpg[0].user_set.add(nu)
            return redirect('login_pat.html')
        else:
            print(form.errors)
    else: 
        form = PatientRegisterForm()
    
    return render(request,'hospital/Patient/register_pat.html',{'form': form})

@login_required
def profile_pat_view(request):
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

def yourhealth_view(request):
    return render(request,'hospital/Patient/yourhealth.html')


# Doctor Related Views

def dash_doc_view(request):
    doc=Doctor.objects.get(user_id=request.user.id)
    patcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()
    appcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    det=[]
    for c in Appointment.objects.filter(status=False,doctorId=doc.id).all():
        p=Patient.objects.filter(id=c.patientId).first()
        if p:
            det.append([p.firstname,c.description,c.appointmentDate,c.link,c.id])
    return render(request,'hospital/Doctor/dashboard_doc.html',{'app':det,'patcount':patcount,'appcount':appcount})

@login_required
def dash_doc_approve_view(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('dashboard_doc.html'))

def bookapp_doc_view(request):
    doc=Doctor.objects.get(user_id=request.user.id)
    det=[]
    for c in Appointment.objects.filter(status=True,doctorId=doc.id).all():
        p=Patient.objects.filter(id=c.patientId).first()
        if p:
            det.append([p.firstname,c.description,c.appointmentDate,c.link])
    if request.method=="POST":
        p_form = PatientAppointmentForm(request.POST, request.FILES, instance=doc)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile_doc.html')
    return render(request,'hospital/Doctor/bookapp_doc.html',{'app':det})

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
            nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))
            doc = Doctor(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        department=form.cleaned_data.get('department'),
                        age=form.cleaned_data.get('age'),
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
            print(form.errors)
    else: 
        form = DoctorRegisterForm()
    
    return render(request,'hospital/Doctor/register_doc.html',{'form': form})



@login_required
def profile_doc_view(request):
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
    

def yourhealth_doc_view(request):
    return render(request,'hospital/Doctor/yourhealth_doc.html')

def medicalreport_doc_view(request):
    return render(request,'hospital/Doctor/medicalreport_doc.html')

@login_required
def doc_approve_appoint_view(request):
    #those whose approval are needed from a particular Doctor
    doc=Doctor.objects.get(user_id=request.user.id)
    det=[]
    for c in Appointment.objects.filter(status=False,doctorId=doc.id).all():
        d=Doctor.objects.filter(id=c.doctorId).first()
        p=Patient.objects.filter(id=c.patientId).first()
        if d and p:
            det.append([p.firstname,c.description,c.appointmentDate,c.id])
    return render(request,'hospital/Doctor/bookapp_doc.html',{'app':det})

@login_required
def doc_approve_app_view(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('bookapp_doc.html'))








def home_view(request):
    return render(request,'hospital/Home/home.html')


def login_view(request):
    return render(request,'hospital/Home/login.html')

@login_required
def bill_view(request):
    pat = Patient.objects.filter(user_id=request.user.id).first()
    context = {
        'pat': pat
     }
    return render(request,'hospital/Patient/bill.html',context)
    



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




