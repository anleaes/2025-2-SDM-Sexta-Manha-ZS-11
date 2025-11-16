from django.db import models
from condominios.models import Condominio

# Create your models here.
class Bloco(models.Model):
    nome = models.CharField('Nome', max_length=50)
    numero_andares = models.IntegerField('Numero de Andares')
    quantidade_apartamentos = models.IntegerField('Quantidade de Apartamentos')
    ativo = models.BooleanField('Ativo', default=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bloco'
        verbose_name_plural = 'Blocos'
        ordering =['id']
        
    def __str__(self):
        return self.nome