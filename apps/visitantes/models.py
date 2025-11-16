from django.db import models

# Create your models here.
class Visitante(models.Model):
    nome = models.CharField('Nome', max_length=50)
    documento = models.CharField('Documento', max_length=20)
    tipo_visita = models.CharField('Tipo de Visita', max_length=30)
    placa_visitante = models.CharField('Placa do Veículo', max_length=10, blank=True, null=True) 