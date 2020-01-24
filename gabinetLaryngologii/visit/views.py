from sqlite3 import DatabaseError
from time import time
from re import split

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from gabinetLaryngologii import settings
from gabinetLaryngologii.visit.models import Appointment, ConfirmationToken
from gabinetLaryngologii.visit.serializers import AppointmentSerializer, AppointmentUpdateSerializer, \
    AppointmentFinalUpdateSerializer
from gabinetLaryngologii.visit.tokenService import token_generator, decrypt
from gabinetLaryngologii.visit.celeryTasks import send_confirmation_email


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = None
    http_method_names = ['get', 'post']

    def get_queryset(self):
        if self.request.method == 'GET':
            return Appointment.objects.filter(appointment_status="Open")
        return super().get_queryset()

    @action(methods=['post'], detail=True)
    # TODO USE VERB FORMS
    def reservation(self, request, pk):
        serializer = AppointmentUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person_data = serializer.data
        appointment = self.get_object()
        if appointment.appointment_status != "Open":
            return Response({"message": "Ta data wizyta została już zarezerwowana."}, status=400)

        appointment.appointment_status = "Waiting for confirmation"
        appointment.name = person_data['name']
        appointment.surname = person_data['surname']
        appointment.email = person_data['email']
        appointment.save()

        token = token_generator(person_data["email"])
        subscription_confirmation_url = settings.CONFIRMATION_URL + "?token=" + token + "&id=" + str(appointment.id)

        confirmation_token = ConfirmationToken(appointment=appointment,
                                               confirmation_link=token)
        confirmation_token.save()

        # send_confirmation_email.delay(person_data["email"], subscription_confirmation_url,
        #                               appointment.appointment_time, appointment.appointment_date)
        return Response(
            {"message": "Został wysłany E-mail potwierdzający wizytę. Potwierdź wizytę w ciągu 12 godizn."},
            status=200)

    @action(methods=['post'], detail=True)
    # TODO USE VERB FORMS
    def reservation_confirmation(self, request, pk):
        serializer = AppointmentFinalUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        person_data = serializer.data
        token = person_data["token"]
        try:
            confirmation_token = ConfirmationToken.objects.get(confirmation_link=token)
        except:
            return Response({"message": "Błędny link potwierdzający."}, status=400)

        decrypted_data = decrypt(token)
        email, token_crated_time = split('SEPARATOR', decrypted_data)

        appointment = self.get_object()
        if appointment.email != email:
            return Response({"message": "Błędny link potwierdzający."}, status=400)

        current_time = time()
        life_of_token = current_time - float(token_crated_time)
        if life_of_token >= settings.EXPIRATION_TOKEN_TIME:
            return Response({"message": "Twój link potwierdzający wygasł."}, status=400)

        if appointment.appointment_status != "Waiting for confirmation":
            return Response({"message": "Tą wizytę już potwierdzono."}, status=400)

        appointment.appointment_status = "Reserved"
        appointment.save()

        confirmation_token.delete()
        return Response({"message": "Twoja wizyta została potwierdzona! Dziękujemy!"}, status=200)
