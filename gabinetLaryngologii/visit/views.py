from django.shortcuts import render
from rest_framework import viewsets, views

from gabinetLaryngologii.visit.models import Appointment
from gabinetLaryngologii.visit.serializers import AppointmentSerializer, AppointmentSerializerUpdate


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    http_method_names = ['get', 'patch']


class AppointmentView(views.APIView):

    def patch(self, request):
        serializer = AppointmentSerializerUpdate(data=request.data)
        serializer.is_valid(raise_exception=True)

        print("działa")
        return None
