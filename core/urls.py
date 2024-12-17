from django.urls import path, include
from .views import (
    AircraftViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'aircrafts', AircraftViewSet, basename='aircrafts')
urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', AuthViewSet.as_view({'get': 'list', 'post': 'create'}), name='auth_list'),
]
