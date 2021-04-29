from django.contrib import admin
from .models import Doctor,Admin,Patient,Appointment,PatHealth,PatAdmit

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Admin)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(PatHealth)
admin.site.register(PatAdmit)