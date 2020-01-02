from django.shortcuts import render
from rest_framework import viewsets

from gabinetLaryngologii.visit.models import Appointment
from gabinetLaryngologii.visit.serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    http_method_names = ['get', 'patch']
