from django.urls import path, include
from .views import (
    AircraftViewSet,
    SeatViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'aircrafts', AircraftViewSet, basename='aircrafts')
router.register(r'seats', SeatViewSet, basename='seats')
urlpatterns = [
    path('', include(router.urls)),
]
