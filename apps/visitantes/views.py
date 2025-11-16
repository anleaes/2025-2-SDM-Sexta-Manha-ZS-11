from django.shortcuts import render
from .models import Visitante
from .serializer import VisitanteSerializer

# Create your views here.
class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer