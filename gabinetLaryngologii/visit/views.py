from time import time
from re import split

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import viewsets

from gabinetLaryngologii.visit.models import Appointment, ConfirmationToken
from gabinetLaryngologii.visit.serializers import AppointmentSerializer, AppointmentUpdateSerializer, \
    AppointmentFinalUpdateSerializer
from gabinetLaryngologii.visit.token_handler import token_generator, encrypt, decrypt
from gabinetLaryngologii.visit.celery_tasks import send_confirmation_email, remove_old_appointments_from_db


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = None
    http_method_names = ['get', 'patch']

    @csrf_exempt
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True

        if "name" in request.data:

            serializer = AppointmentUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            appointment = self.get_object()
            if appointment.appointment_status != "open":
                return Response({"message": "Ta data wizyta została już zarezerwowana."}, status=400)

            appointment.appointment_status = "Waiting for confirmation"
            appointment.save()

            person_data = serializer.data
            token = token_generator(person_data["email"])
            subscription_confirmation_url = "https://gabinetlogopedyczny.mglernest.now.sh/confirmation/" \
                                            + "?token=" + token + "&id=" + str(appointment.id)

            confirmation_token = ConfirmationToken(appointment=appointment,
                                                   confirmation_link=token)
            confirmation_token.save()

            send_confirmation_email.delay(person_data["email"], subscription_confirmation_url,
                                          appointment.appointment_time,
                                          appointment.appointment_date)
            self.update(request, *args, **kwargs)
            return Response(
                {"message": "Został wysłany E-mail potwierdzający wizytę. Potwierdź wizytę w ciągu 12 godizn."},
                status=200)
        elif "token" in request.data:

            serializer = AppointmentFinalUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            person_data = serializer.data
            token = person_data["token"]

            if ConfirmationToken.objects.filter(confirmation_link=token).count() == 0:
                return Response({"message": "Błędny link potwierdzający."}, status=400)

            decrypted_data = decrypt(token)
            email, token_crated_time = split('SEPARATOR', decrypted_data)
            current_time = time()
            life_of_token = current_time - float(token_crated_time)
            if life_of_token >= 43200:
                return Response({"message": "Twój link potwierdzający wygasł."}, status=400)
            appointment = self.get_object()

            if appointment.appointment_status != "Waiting for confirmation":
                return Response({"message": "Tą wizytę już potwierdzono."}, status=400)

            appointment.appointment_status = "Reserved"
            appointment.save()

            self.update(request, *args, **kwargs)
            return Response({"message": "Twoja wizyta została potwierdzona! Dziękujemy!"}, status=200)
        else:
            return Response({"message": "Błąd!"}, status=400)
