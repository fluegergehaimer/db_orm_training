from rest_framework import serializers
from .models import Aircraft


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'
        # read_only_fields = ('aircraft_code',)
