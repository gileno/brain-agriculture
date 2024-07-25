import pytest

from model_bakery import baker

from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse

from brain_agriculture.security.models import User

from brain_agriculture.farmers.constants import PersonTypeChoices
from brain_agriculture.farmers.models import City, Farmer, Culture


@pytest.fixture
def farmer_data():
    city = baker.make(City)
    return {
        'person_type': PersonTypeChoices.PF,
        'document': '252.071.680-02',
        'total_area': 100,
        'arable_area': 50,
        'vegetation_area': 50,
        'city': city,
        'name': 'Farmer Test',
        'farm_name': 'Farm Test',
    }


@pytest.fixture
def user():
    return baker.make(User, email='admin@admin.com')


@pytest.mark.django_db
def test_farmer_detail(farmer_data, user):
    farmer = Farmer.objects.create(**farmer_data)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('farmer-detail', kwargs={'pk': farmer.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['document'] == '25207168002'


@pytest.mark.django_db
def test_farmer_list(farmer_data, user):
    baker.make(Farmer, person_type=PersonTypeChoices.PF, document='25207168002', _quantity=10)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('farmer-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 10
