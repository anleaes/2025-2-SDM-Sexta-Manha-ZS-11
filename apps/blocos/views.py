from .models import Bloco
from rest_framework import viewsets
from .serializer import BlocoSerializer

# Create your views here.
class BlocoViewSet(viewsets.ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer