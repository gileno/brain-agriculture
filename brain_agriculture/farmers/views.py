from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from brain_agriculture.farmers.serializers import CitySerializer, CultureSerializer, FarmerSerializer
from brain_agriculture.farmers.filtersets import CityFilterSet, CultureFilterSet, FarmerFilterSet
from brain_agriculture.farmers.models import City, Culture, Farmer


class CityViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CitySerializer
    queryset = City.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]
    filterset_class = CityFilterSet


class CultureViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CultureSerializer
    queryset = Culture.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]
    filterset_class = CultureFilterSet


class FarmerViewSet(viewsets.ModelViewSet):

    serializer_class = FarmerSerializer
    queryset = Farmer.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = FarmerFilterSet
