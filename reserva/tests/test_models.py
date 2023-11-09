from datetime import date

import pytest
from model_bakery import baker
from reserva.models import Reserva, Petshop


def test_config():
    assert 1 == 1

@pytest.mark.django_db
def test_qtd_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quantidade = 3
    baker.make(
        Reserva,
        quantidade,
        petshop=petshop
    )

    assert petshop.qtd_reservas() == 3

@pytest.fixture
def reserva():
    data = date(2022, 10, 8)
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=data,
        turno='tarde'
    )
    return reserva

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Tom: 2022-10-08 - tarde'