from django.shortcuts import render
from rest_framework import viewsets

from gabinetLogopedyczny.visit.models import Appointment
from gabinetLogopedyczny.visit.serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    http_method_names = ['get', 'patch']
