from rest_framework import viewsets
from .models import Proprietario
from .serializer import ProprietarioSerializer

# Create your views here.
class ProprietarioViewSet(viewsets.ModelViewSet):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer