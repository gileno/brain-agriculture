import django_filters

from brain_agriculture.farmers.models import City, Culture, Farmer


class CityFilterSet(django_filters.FilterSet):

    class Meta:
        model = City
        fields = {
            "state": ["exact"],
            "name": ["icontains"],
        }


class CultureFilterSet(django_filters.FilterSet):

    class Meta:
        model = Culture
        fields = {
            "name": ["icontains"],
        }


class FarmerFilterSet(django_filters.FilterSet):

    class Meta:
        model = Farmer
        fields = {
            "city": ["exact"],
            "name": ["icontains"],
            "farm_name": ["icontains"],
            "document": ["icontains"],
            "person_type": ["exact"],
            "cultures": ["in"],
        }
