from .models import Apartamento
from rest_framework import viewsets
from .serializer import ApartamentoSerializer

# Create your views here.
class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer