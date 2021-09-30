from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ClientSerializer, Office_MFCSerializer
from .models import Office_MFC, Client

from django.http import HttpResponse, JsonResponse, request
from rest_framework.parsers import JSONParser

# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated]

class Office_MFCViewSet(viewsets.ModelViewSet):
    queryset = Office_MFC.objects.all()
    serializer_class = Office_MFCSerializer
    # permission_classes = [IsAuthenticated]


