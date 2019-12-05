from rest_framework import serializers
import re


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()
    message = serializers.CharField(max_length=1000)

    def is_valid(self, raise_exception=True):
        data = self.initial_data
        if not data['name']:
            raise serializers.ValidationError({'message': 'Pole Imię nie może być puste.'})
        if not data['surname']:
            raise serializers.ValidationError({'message': 'Pole Nazwisko nie może być puste.'})
        if not data['email']:
            raise serializers.ValidationError({'message': 'Pole E-mail nie może być puste.'})
        if not data['message']:
            raise serializers.ValidationError({'message': 'Pole Wiadomosc nie może być puste.'})
        if not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", data['email']):
            raise serializers.ValidationError({'message': 'Podaj poprawny adres E-mail.'})

        return True
