from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from gabinetLaryngologii.visit.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ['appointment_status', 'email']


class AppointmentAdmin(ModelAdmin):
    form = AppointmentForm


admin.site.register(Appointment, AppointmentAdmin)