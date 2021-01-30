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
    path('dash/',views.dash_view,name='dashboard.html'),
    path('about/',views.about_view,name='user.html'),
    path('login/',views.login_view,name='typography.html'),
    path('news/',views.news_view,name='notifications.html'),
    path('signup/',views.signup_view,name='tables.html'),
    path('contact_us/',views.contact_us_view,name='icons.html'),
    #path('hospital/', include('hospital.urls')),
    
]
