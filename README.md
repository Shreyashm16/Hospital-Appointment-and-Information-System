# Hospital-Appointment-and-Information-System
#### As demand for an Automatic System in the Health Care Sector are high, we need to develop a unique web app for online OPD Appointment , Registration and Hospital Information System. With automation, doctors & nurses can reach out to more patients in a more efficient way, cutting repetitive tasks likepaperwork.

## Problem Statement
At present, there is no platform which can have all virtual functionalities such as video call diagnosis help, online emergency facility & online monitoring patients, One-to-one communication in between patient & doctor virtually, etc.
So, we have focussed on creating an integrated platform that can assimilate the patients and doctors under a single roof which is under a the admin supervision. 
This is in accordance with a problem raised by the AYUSH ministry in SIH (Smart India Hackathon) 2020.

## Motivation
As demands of an automatic system in the healthcare sector are high, we need to develop a unique web app for online OPD Appointment , Registration and Hospital Information System. 
We have focussed on creating an integrated platform that can assimilate patients and doctors under a single roof which is under admin supervision. This would bring transparency and decentralisation in the hospital management which is really uncommon as of now.
![image](https://user-images.githubusercontent.com/56602020/116561169-b1fa8e00-a91f-11eb-98a4-9bfb67f8d39a.png)

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

* Signup their account. Then Login (No approval Required).
* Can register/view/approve/reject/delete doctor (approve those doctor who applied for job in their hospital).
* Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
* Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge and other charge).
* Can view/book/approve Appointment (approve those appointments which is requested by patient).
* ![image](https://user-images.githubusercontent.com/56602020/116562228-9b086b80-a920-11eb-937f-32d6d4db10a3.png)


## Doctor

* Apply for job in hospital. Then Login (Approval required by hospital admin, Then only doctor can login).
* Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
* Can view their discharged(by admin) patient list.
* Can view their Appointments, booked by admin.
* Can delete their Appointment, when doctor attended their appointment.
* ![image](https://user-images.githubusercontent.com/56602020/116562079-8035f700-a920-11eb-992b-7f335a58eed7.png)


## Patient

* Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
* Can view assigned doctor's details like ( specialization, mobile, address).
* Can view their booked appointment status (pending/confirmed by admin).
* Can book appointments.(approval required by admin).
* Can view/download Invoice pdf (Only when that patient is discharged by admin).
* ![image](https://user-images.githubusercontent.com/56602020/116561436-f0904880-a91f-11eb-8afd-5ad9bcce1903.png)


## Problem Modules

Module 1 : Creation of Basic outline structure of the Project (Static files generation, linking with Backend,etc)

Module 2 : Almost completion of front-end part, Form Creations,etc.

Module 3: Database linking of app & completion of left-over Backend Functionalities.

Module 4: Deployment & Hosting on a Web Server.

## HOW TO RUN THIS PROJECT

* Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python).
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

* There is no Approval required for admin account. So you can disable admin signup process and use any logic like creating superuser.

## Feedback

For any queries, reach out to the Developers :
* [Siddharth Pandey](mailto:siddharth25pandey@gmail.com) (**Front End & Back End**)
* [Shreyash Mishra](mailto:shreyashm1601@gmail.com) (**Front End & Back End**)
* [Priyam Bajpai](mailto:priyambajpai@yahoo.in) (**Front End & Back End**)
* [Naveen Kumar](mailto:naveenkumar.k19@gmail.com) (**Front End**)
* [Yaduraj Deshmukh](mailto:yadurajdeshmukh2.303@gmail.com) (**Front End**)
 
 
    
