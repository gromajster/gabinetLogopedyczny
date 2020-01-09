from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from gabinetLaryngologii.material.serializers import MediaSerializer
from .models import Media


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    http_method_names = ['get']

