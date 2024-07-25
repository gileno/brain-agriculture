import pytest

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from model_bakery import baker

from brain_agriculture.farmers.models import Farmer
from brain_agriculture.farmers.constants import PersonTypeChoices


@pytest.mark.django_db
def test_cpf_validation_ok():
    cpf = '252.071.680-02'
    baker.make(
        Farmer,
        document=cpf,
        person_type=PersonTypeChoices.PF,
        total_area=100,
        arable_area=50,
        vegetation_area=50,
    )


@pytest.mark.django_db
def test_cpf_validation_error():
    cpf = '000.000.680-02'
    with pytest.raises(ValidationError):
        baker.make(
            Farmer,
            document=cpf,
            person_type=PersonTypeChoices.PF,
            total_area=100,
            arable_area=50,
            vegetation_area=50,
        )


@pytest.mark.django_db
def test_cnpj_validation_ok():
    cnpj = '99.147.398/0001-50'
    baker.make(
        Farmer,
        document=cnpj,
        person_type=PersonTypeChoices.PJ,
        total_area=100,
        arable_area=50,
        vegetation_area=50,
    )


@pytest.mark.django_db
def test_cnpj_validation_error():
    cnpj = '00.000.000/0001-50'
    with pytest.raises(ValidationError):
        baker.make(
            Farmer,
            document=cnpj,
            person_type=PersonTypeChoices.PJ,
            total_area=100,
            arable_area=50,
            vegetation_area=50,
        )


@pytest.mark.django_db
def test_total_area_validation_error():
    cnpj = '99.147.398/0001-50'
    with pytest.raises(IntegrityError):
        baker.make(
            Farmer,
            document=cnpj,
            person_type=PersonTypeChoices.PJ,
            total_area=100,
            arable_area=100,
            vegetation_area=50,
        )
