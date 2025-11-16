from .models import Bloco
from rest_framework import serializers

class BlocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = '__all__'