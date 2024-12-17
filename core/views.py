from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Aircraft, Seat
from .serializers import AircraftSerializer, SeatSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all().prefetch_related('seats')
    serializer_class = AircraftSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    filterset_fields = ['aircraft_code', 'model']


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['aircraft_code', 'fare_conditions']
    search_fields = ['seat_no', 'fare_conditions']

    def get_queryset(self):
        return super().get_queryset().select_related('aircraft_code')
