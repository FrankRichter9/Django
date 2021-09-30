from rest_framework import serializers

from .models import Office_MFC, Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = (
            'user',
            'full_name',
            'addres',
            'passport',
            'phone-number'
        )

class Office_MFCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Office_MFC
        fields = (
            'office_name',
            'addres',
            'phone_number'
        )

