from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Sum

from brain_agriculture.farmers.serializers import CitySerializer, CultureSerializer, FarmerSerializer
from brain_agriculture.farmers.filtersets import CityFilterSet, CultureFilterSet, FarmerFilterSet
from brain_agriculture.farmers.models import City, Culture, Farmer
from brain_agriculture.farmers.constants import StateChoices


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

    @action(detail=False, methods=['GET'])
    def data(self, request):
        total = Farmer.objects.count()
        total_area = Farmer.objects.aggregate(total=Sum('total_area'))['total']
        vegetation_area = Farmer.objects.aggregate(total=Sum('vegetation_area'))['total']
        arable_area = Farmer.objects.aggregate(total=Sum('arable_area'))['total']
        cultures = []
        for culture in Culture.objects.all():
            cultures.append({
                'culture': culture.name,
                'total': Farmer.objects.filter(cultures__in=[culture]).count(),
            })
        states = []
        for state in StateChoices:
            states.append({
                'state': state,
                'total': Farmer.objects.filter(city__state=state).count()
            })
        
        return Response(
            data={
                'total': total,
                'total_area': total_area,
                'vegetation_area': vegetation_area,
                'arable_area': arable_area,
                'cultures': cultures,
                'states': states,
            }
        )
