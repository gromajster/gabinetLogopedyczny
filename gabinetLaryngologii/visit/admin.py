from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from gabinetLaryngologii.visit.models import Appointment, ConfirmationToken

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ['appointment_status', 'email', 'surname', 'name']


class AppointmentAdmin(ModelAdmin):
    form = AppointmentForm
    list_display = (
        'name', 'surname', 'email', 'day', 'month', 'year', 'appointment_time', 'appointment_status')
    list_filter = ('appointment_status', 'appointment_time', 'appointment_date')
    search_fields = ('name', 'surname', 'email')
    date_hierarchy = 'appointment_date'
    ordering = ('appointment_date',)


admin.site.register(Appointment, AppointmentAdmin)

admin.site.register(ConfirmationToken)
