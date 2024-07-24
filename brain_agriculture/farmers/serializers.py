from rest_framework import serializers

from brain_agriculture.farmers.models import City, Farmer, Culture


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = [
            'id',
            'name',
            'state',
            'is_active',
            'created_on',
            'updated_on',
        ]


class CultureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Culture
        fields = [
            'id',
            'name',
            'is_active',
            'created_on',
            'updated_on',
        ]


class FarmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farmer
        fields = [
            'id',
            'name',
            'farm_name',
            'person_type',
            'document',
            'city',
            'total_area',
            'arable_area',
            'vegetation_area',
            'cultures',
            'is_active',
            'created_on',
            'updated_on',
        ]
