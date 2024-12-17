from rest_framework import serializers
from .models import Aircraft, Seat


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ['seat_no', 'fare_conditions']


class AircraftSerializer(serializers.ModelSerializer):
    seats_count = serializers.SerializerMethodField()
    seats_list = SeatSerializer(many=True, source='seats')

    class Meta:
        model = Aircraft
        fields = ['aircraft_code', 'model', 'range', 'seats_count', 'seats_list']
        # read_only_fields = ('aircraft_code',)

    def get_seats_count(self, obj):
        return obj.seats.count()

    def get_seats_list(self, obj):
        return obj.seats.order_by('seat_no')
