from .models import Garagem
from rest_framework import viewsets
from .serializer import GaragemSerializer   

# Create your views here.
class GaragemViewSet(viewsets.ModelViewSet):
    queryset = Garagem.objects.all()
    serializer_class = GaragemSerializer
