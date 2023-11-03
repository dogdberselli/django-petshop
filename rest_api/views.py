from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_api.serializers import AgendamentoModelSerializer, PetshopModelSerializer
from reserva.models import Reserva, Petshop
from base.models import Contato
# Create your views here.

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class PetshopModelViewSet(ModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'Hello': 'World API'})

@api_view()
def contato(request):
    consulta = Contato.objects.all()
    dados = []
    for contato in consulta:
        dado = {
            'id': contato.id,
            'nome': contato.nome,
            'email': contato.email,
            'mensagem': contato.mensagem,
        }
        dados.append(dado)
    return Response(dados)