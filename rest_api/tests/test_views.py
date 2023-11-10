import pytest
import datetime
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer

@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste', 'email': 'test@example.com',
        'nome_pet': 'pet test', 'data': hoje, 'turno': 'manhã',
        'tamanho': 0, 'observacoes': '', 'petshop': petshop.pk,
    }

@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.fixture
def agendamento():
    return baker.make(Reserva)

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    assert resposta.status_code == 201

@pytest.mark.django_db
def test_remover_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    agendamento_id = resposta.data['id']
    resposta_remover = cliente.delete(f'/api/agendamento/{agendamento_id}')
    assert resposta_remover.status_code == 204

@pytest.mark.django_db
def test_atualizar_agendamento(usuario, dados_agendamento):
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    agendamento_id = resposta.data['id']
    novos_dados = {
        'nome': 'nome example', 'email': 'test2@example.com',
        'nome_pet': 'pet test', 'data': hoje, 'turno': 'manhã',
        'tamanho': 1, 'observacoes': 'alterado', 'petshop': petshop.pk,
    }
    atualiza_agendamento = cliente.put(f'/api/agendamento/{agendamento_id}', novos_dados)
    assert atualiza_agendamento.status_code == 200

@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agendamento')
    assert len(resposta.data['results']) == 1

@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    assert len(resposta.data['results']) == 0