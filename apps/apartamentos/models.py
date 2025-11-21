from django.db import models
from proprietarios.models import Proprietario
from blocos.models import Bloco

# Create your models here.
class Apartamento(models.Model):
    numero = models.CharField(max_length=10)
    andar = models.IntegerField()
    area_m2 = models.FloatField()
    ocupado = models.BooleanField(default=False)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    dono = models.ManyToManyField(Proprietario)
    
    class Meta:
        verbose_name = "Apartamento"
        verbose_name_plural = "Apartamentos"
        ordering = ['id']
    
    def __str__(self):
        return self.numero