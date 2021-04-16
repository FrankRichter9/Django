from rest_framework import serializers

from .models import Service_rendered, Service, Documentation




class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Service
        fields = (
           'name',
           'comment'
        )



