# Hospital-Appointment-and-Information-System

## Problem Statement
At present, there is no platform which can have all virtual functionalities such as video call diagnosis help, online emergency facility & online monitoring patients, One-to-one communication in between patient & doctor virtually, etc.
So, we have focused on creating an integrated platform that can assimilate the patients and doctors under a single roof which is under a the admin supervision. 
This is in accordance with a problem raised by the AYUSH ministry in SIH (Smart India Hackathon) 2020.

## Motivation
As demand of an automatic system in the healthcare sector are high, we need to develop a unique web app for online OPD Appointment , Registration and Hospital Information System. We have focused on creating an integrated platform that can assimilate patients and doctors under a single roof which is under admin supervision. This would bring transparency and decentralization in the hospital management which is really uncommon as of now.

## Use Case Diagram for this Project
![homepage snap 1](https://github.com/Shreyashm16/Hospital-Appointment-and-Information-System/blob/main/Screenshot/Usecase_diagram.png)
## Screenshots
### Homepage
![homepage snap 1](https://github.com/Shreyashm16/Hospital-Appointment-and-Information-System/blob/main/Screenshot/home_1.PNG)

![homepage snap 2](https://github.com/Shreyashm16/Hospital-Appointment-and-Information-System/blob/main/Screenshot/home_2.PNG)

### Loginpage
![login snap](https://github.com/Shreyashm16/Hospital-Appointment-and-Information-System/blob/main/Screenshot/login_page.PNG)

### Admin Dashboard
![Admin snap](https://github.com/Shreyashm16/Hospital-Appointment-and-Information-System/blob/main/Screenshot/adm.PNG)

### Patient Dashboard

![Patient snap](https://github.com/Shreyashm16/Hospital-Appointment-and-Information-System/blob/main/Screenshot/pat.PNG)
### Doctor Dashboard

![Docor snap](https://github.com/Shreyashm16/Hospital-Appointment-and-Information-System/blob/main/Screenshot/doc.PNG)

## Functional Description

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
* ## Admin

* Signup their account. Then Login (Approval required by hospital Super admin, Then only Admin can login).
* Can register/view/approve/ (approve those doctor who applied for job in their hospital).
* Can admit/view/approve/discharge patient (discharge patient when treatment is done).
* Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge and other charge).
* Can view/book/approve Appointment (approve those appointments which is requested by patient).




## Doctor

* Apply for job in hospital. Then Login (Approval required by hospital admin, Then only doctor can login).
* Can only view their patient details (symptoms, name ) assigned to that doctor by admin.
* Can view their discharged (by admin) patient list.
* Can generate Video Calling Link with Patients.
* Can view their Appointments, booked by admin.
* Can delete their Appointment, when doctor attended their appointment.


## Patient

* Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
* Can view assigned doctor's details like ( specialization, mobile, address).
* Can view their booked appointment status (pending/confirmed by admin).
* Can book appointments.(approval required by admin).
* Can view/download Invoice pdf (Only when that patient is discharged by admin).


## Problem Modules

* Module 1 : Creation of Basic outline structure of the Project (Static files generation, linking with Backend,etc)
* Module 2 : Almost completion of front-end part, Form Creations,etc.
* Module 3: Database linking of app & completion of left-over Backend Functionalities.
* Module 4: Deployment & Hosting on a Web Server.

## HOW TO RUN THIS PROJECT

* Install Python(3.7.6) (Don't Forget to Tick Add to Path while installing Python).
* Open Terminal and Execute Following Commands :
    ```
    pip install django==3.0.5
    pip install django-widget-tweaks
    pip install xhtml2pdf
    ```

* Download This Project Zip Folder and Extract it
* Move to project folder in Terminal. Then run following Commands :
   ```
    py manage.py makemigrations
    py manage.py migrate
    py manage.py runserver
    ```

* Now enter following URL in Your Browser Installed On Your Pc

    ```http://127.0.0.1:8000/  ```
 
 ## CHANGES REQUIRED FOR CONTACT US PAGE
 
* In settins.py file, You have to give your email and password
  ```
  EMAIL_HOST_USER = 'youremail@gmail.com'
  EMAIL_HOST_PASSWORD = 'your email password'
  EMAIL_RECEIVING_USER = 'youremail@gmail.com'
  ```

* Login to gmail through host email id in your browser and open following link and turn it ON
  
 ``` https://myaccount.google.com/lesssecureapps ```
 
 
## Drawbacks/LoopHoles
* Unsupported display feature in Safari Browser
* User need Agora app for accessing the video calling facility through mobile/ IOS Device.

## Feedback

For any queries, reach out to the Developers :
* [Siddharth Pandey](mailto:siddharth25pandey@gmail.com) (**Front End & Back End**)
* [Shreyash Mishra](mailto:shreyashm1601@gmail.com) (**Front End & Back End**)
* [Priyam Bajpai](mailto:priyambajpai@yahoo.in) (**Front End & Back End**)
* [Naveen Kumar](mailto:naveenkumar.k19@gmail.com) (**Front End & Back End**)
* [Yaduraj Deshmukh](mailto:yadurajdeshmukh2.303@gmail.com) (**Front End & Back End**)

##
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/siddharth25pandey/)[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://GitHub.com/siddharth25pandey/)
 
 
    
