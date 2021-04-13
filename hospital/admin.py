from django.contrib import admin
from .models import Doctor,Admin,Patient,Appointment

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Admin)
admin.site.register(Patient)
admin.site.register(Appointment)