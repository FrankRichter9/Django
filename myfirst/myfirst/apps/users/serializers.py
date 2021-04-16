from rest_framework import serializers

from .models import Organization, Office_Organization


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'activity'
        )

class Office_OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Office_Organization
        fields = (
            'id',
            'organization',
            'addres',
            'phone_number'
        )

