from .models import Proprietario
from rest_framework import serializers

class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = '__all__'