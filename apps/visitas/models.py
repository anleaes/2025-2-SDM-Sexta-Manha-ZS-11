from django.db import models
from visitantes.models import Visitante
from apartamentos.models import Apartamento
from proprietarios.models import Proprietario

# Create your models here.
class Visita(models.Model):
    dia = models.DateField()
    hora = models.TimeField()
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        ordering = ['id']
        
    def __str__(self):
        return self.visitante.nome    