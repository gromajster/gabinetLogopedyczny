from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import viewsets, views, status

from gabinetLaryngologii.visit.celery_tasks import send_confirmation_email
from gabinetLaryngologii.visit.models import Appointment
from gabinetLaryngologii.visit.serializers import AppointmentSerializer
from gabinetLaryngologii.visit.token_handler import token_generator, encrypt


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    http_method_names = ['get', 'patch']

    def update(self, request, *args, **kwargs):
        serializer = AppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person_data = serializer.data

        token = token_generator(person_data["email"])
        subscription_confirmation_url = "https://gabinetlogopedyczny.mglernest.now.sh/confirmation/" + "?token=" + token

        send_confirmation_email.delay(person_data["email"], subscription_confirmation_url)

        return Response({"message": "Został wysłany E-mail potwierdzający wizytę."}, status=200)
