from django.db import models

# Create your models here.
class Condominio(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.CharField('Endereco', max_length=100)
    quantidade_blocos = models.IntegerField('Quantidade de Blocos')
    ativo = models.BooleanField('Ativo', default=True)
        
    class Meta:
        verbose_name = 'Condominio'
        verbose_name_plural = 'Condominios'
        ordering =['id']

    def __str__(self):
        return self.nome