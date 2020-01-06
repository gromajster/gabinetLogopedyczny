from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from gabinetLaryngologii.visit.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ['appointment_status', 'email', 'surname']


class AppointmentAdmin(ModelAdmin):
    form = AppointmentForm
    list_display = ('surname', 'email', 'appointment_date', 'appointment_time', 'appointment_status')
    list_filter = ('appointment_status', 'appointment_time', 'appointment_date')
    search_fields = ('surname', 'email')
    date_hierarchy = 'appointment_date'
    ordering = ('appointment_date',)


admin.site.register(Appointment, AppointmentAdmin)
