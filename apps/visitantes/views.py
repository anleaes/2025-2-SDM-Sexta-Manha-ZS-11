from rest_framework import viewsets
from .models import Visitante
from .serializer import VisitanteSerializer

# Create your views here.
class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer