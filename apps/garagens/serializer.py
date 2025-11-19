from .models import Garagem
from rest_framework import serializers

class GaragemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garagem
        fields = '__all__'