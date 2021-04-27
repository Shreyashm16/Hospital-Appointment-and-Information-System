# Hospital-Appointment-and-Information-System
As demands of an Automatic System in the Health Care Sector are high, we need to develop a unique web app for online OPD Appointment , Registration and Hospital Information System.
## Steps to start
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
## Motivation
As demands of an automatic system in the healthcare sector are high, we need to develop a unique web app for online OPD Appointment , Registration and Hospital Information System. 
We have focussed on creating an integrated platform that can assimilate patients and doctors under a single roof which is under admin supervision. This would bring transparency and decentralisation in the hospital management - which is really uncommon as of now.

## Problem Statement
At present, there is no platform which can have all virtual functionalities such as video call diagnosis help, online emergency facility & online monitoring patients, One-to-one communication in between patient & doctor virtually, etc.
 
So, we have focussed on creating an integrated platform that can assimilate the patients and doctors under a single roof which is under a the admin supervision. 

This is in accordance with a problem raised by the AYUSH ministry in SIH (Smart India Hackathon) 2020.

## Problem Solution & Functional Description

Features to Include :

* Secure Login Authentication (Signup and then Login).
* Emergency Registration & Online OPD Appointment.
* Special facilities for older age people like minutes of last appointments and automatic slot booking.
* Medical Lab Report of Present Diagnosis
* Automatic expenses calculator for medicines prescribed in form of Invoice type (view/download).
* Admin access for proper management of the whole system.
* COVID vaccine tracking, availability and appointments.*
* Video/Normal Call and chatting facility for COVID patients surveillance.
* Medical History of the Patient (Database including aadhar)*
* Feedback System for Patients.

## Problem Modules

Module 1 : Creation of Basic outline structure of the Project (Static files generation, linking with Backend,etc)

Module 2 : Almost completion of front-end part, Form Creations,etc.

Module 3: Database linking of app & completion of left-over Backend Functionalities.

Module 4: Deployment & Hosting on a Web Server.


## Functions

## Admin

* Signup their account. Then Login (No approval Required).
* Can register/view/approve/reject/delete doctor (approve those doctor who applied for job in their hospital).
* Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
* Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge and other charge).
* Can view/book/approve Appointment (approve those appointments which is requested by patient).

## Doctor

* Apply for job in hospital. Then Login (Approval required by hospital admin, Then only doctor can login).
* Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
* Can view their discharged(by admin) patient list.
* Can view their Appointments, booked by admin.
* Can delete their Appointment, when doctor attended their appointment.

## Patient

* Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
* Can view assigned doctor's details like ( specialization, mobile, address).
* Can view their booked appointment status (pending/confirmed by admin).
* Can book appointments.(approval required by admin).
* Can view/download Invoice pdf (Only when that patient is discharged by admin).

## HOW TO RUN THIS PROJECT

* Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python).
* Open Terminal and Execute Following Commands :

    pip install django==3.0.5
    pip install django-widget-tweaks
    pip install xhtml2pdf

* Download This Project Zip Folder and Extract it
* Move to project folder in Terminal. Then run following Commands :

    py manage.py makemigrations
    py manage.py migrate
    py manage.py runserver

* Now enter following URL in Your Browser Installed On Your Pc

    http://127.0.0.1:8000/  
 
 ## CHANGES REQUIRED FOR CONTACT US PAGE
 
* In settins.py file, You have to give your email and password
  
  EMAIL_HOST_USER = 'youremail@gmail.com'
  EMAIL_HOST_PASSWORD = 'your email password'
  EMAIL_RECEIVING_USER = 'youremail@gmail.com'

* Login to gmail through host email id in your browser and open following link and turn it ON
  
  https://myaccount.google.com/lesssecureapps
 
 
## Drawbacks/LoopHoles

* Any one can be Admin. There is no Approval required for admin account. So you can disable admin signup process and use any logic like creating superuser.
* There should be at least one doctor in hospital before admitting patient. So first add doctor.
* On update page of doctor/patient you must have to update password.

## Disclaimer

This project is developed for demo purpose and it's not supposed to be used in real application.

## Feedback
 
 
    
