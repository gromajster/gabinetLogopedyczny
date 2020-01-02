from rest_framework import serializers

from gabinetLaryngologii.visit.models import Appointment


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'email', 'appointment_date', 'appointment_time', 'appointment_status']
