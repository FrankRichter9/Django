from django.shortcuts import render
from rest_framework import viewsets

from .serializers import OrganizationSerializer, Office_OrganizationSerializer
from .models import Organization, Office_Organization

# Create your views here.


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class Office_OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Office_Organization.objects.all()
    serializer_class = Office_OrganizationSerializer

