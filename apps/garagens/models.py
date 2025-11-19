from django.db import models
from apartamentos.models import Apartamento

# Create your models here.
class Garagem(models.Model):
    numero_vaga = models.CharField(max_length=10)   
    coberta = models.BooleanField(default=False)
    placa_veiculo = models.CharField(max_length=15)
    disponivel = models.BooleanField(default=True)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Garagem"
        verbose_name_plural = "Garagens"
        ordering = ['id']
        
    def __str__(self):
        return self.numero_vaga    