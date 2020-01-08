import re

from rest_framework import serializers

from gabinetLaryngologii.visit.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'day', 'month', 'year', 'appointment_time', 'appointment_status', 'name', 'surname', 'email')
        extra_kwargs = {
            'name': {'write_only': True},
            'surname': {'write_only': True},
            'email': {'write_only': True}
        }

    def is_valid(self, raise_exception=True):
        data = self.initial_data
        if not data['name']:
            raise serializers.ValidationError({'message': 'Pole Imię nie może być puste.'})
        if not data['surname']:
            raise serializers.ValidationError({'message': 'Pole Nazwisko nie może być puste.'})
        if not data['email']:
            raise serializers.ValidationError({'message': 'Pole E-mail nie może być puste.'})
        if not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", data['email']):
            raise serializers.ValidationError({'message': 'Podaj poprawny adres E-mail.'})

        return super().is_valid()
