from django.db import models
from condominios.models import Condominio

# Create your models here.
class Product(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cargo = models.CharField('Cargo', max_length=50)
    salario = models.FloatField('Salario')
    ativo = models.BooleanField('Ativo', default=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering =['id']

    def __str__(self):
        return self.nome