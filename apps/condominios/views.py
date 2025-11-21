from django.shortcuts import render
from rest_framework import viewsets
from .models import Condominio
from .serializer import CondominioSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'endereco']