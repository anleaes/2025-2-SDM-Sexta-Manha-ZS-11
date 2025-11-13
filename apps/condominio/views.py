from django.shortcuts import render
from rest_framework import viewsets
from .models import Condominio
from .serializer import CondominioSerializer

# Create your views here.
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer  