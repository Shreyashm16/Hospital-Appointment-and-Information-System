"""hospital_appointment_and_information_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from hospital import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('dash_pat/',views.dash_view,name='dashboard.html'),
    path('bookapp_pat/',views.bookapp_view,name='bookapp.html'),
    path('calladoc_pat/',views.calladoc_view,name='calladoc.html'),
    path('feedback_pat/',views.feedback_view,name='feedback.html'),
    path('medicalreport_pat/',views.medicalreport_view,name='medicalreport.html'),
    path('profile_pat/',views.profile_view,name='profile.html'),
    path('yourhealth_pat/',views.yourhealth_view,name='yourhealth.html'),
    path('home/',views.home_view,name='home.html'),
    path('dash_doc/',views.dash_doc_view,name='dashboard_doc.html'),
    path('bookapp_doc/',views.bookapp_doc_view,name='bookapp_doc.html'),
    path('calladoc_doc/',views.calladoc_doc_view,name='calladoc_doc.html'),
    path('feedback_doc/',views.feedback_doc_view,name='feedback_doc.html'),
    path('medicalreport_doc/',views.medicalreport_doc_view,name='medicalreport_doc.html'),
    path('profile_doc/',views.profile_doc_view,name='profile_doc.html'),
    path('yourhealth_doc/',views.yourhealth_doc_view,name='yourhealth_doc.html'),
    path('dash_adm/',views.dash_adm_view,name='dashboard_adm.html'),
    path('bookapp_adm/',views.bookapp_adm_view,name='bookapp_adm.html'),
    path('calladoc_adm/',views.calladoc_adm_view,name='calladoc_adm.html'),
    path('feedback_adm/',views.feedback_adm_view,name='feedback_adm.html'),
    path('medicalreport_adm/',views.medicalreport_adm_view,name='medicalreport_adm.html'),
    path('profile_adm/',views.profile_adm_view,name='profile_adm.html'),
    path('yourhealth_adm/',views.yourhealth_adm_view,name='yourhealth_adm.html'),
    path('home/',views.home_view,name='home.html'),
    #path('services/',views.services_view,name='services.html'),
    #path('contactus/',views.contactus_view,name='contactus.html'),
    #path('news/',views.news_view,name='news.html'),
    path('login/',views.login_view,name='login.html'),
    #path('hospital/', include('hospital.urls')),
    
]
