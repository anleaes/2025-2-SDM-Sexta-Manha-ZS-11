from.models import Visita
from rest_framework import viewsets
from .serializer import VisitaSerializer

# Create your views here.
class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
