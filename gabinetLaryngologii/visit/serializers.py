from rest_framework import serializers

from gabinetLogopedyczny.visit.models import Appointment


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'day', 'month', 'year', 'appointment_time', 'appointment_status']
