from django.db import models

# Create your models here.
class Proprietario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.CharField('Email', max_length=50)
    telefone = models.CharField('Telefone', max_length=15)
    data_entrada = models.DateField('Data de Entrada')
    