from .models import Visita
from rest_framework import serializers

class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__'