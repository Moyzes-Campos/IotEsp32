from django.db import models
from django.shortcuts import reverse


# Create your models here.
class EstadoBotao(models.Model):
    jsonfield = models.JSONField()

    def get_absolute_url(self):
        return reverse('index')


class ProducaoMachine1(models.Model):
    dia = models.DateField(auto_now_add=True)
    dia_e_hora = models.DateTimeField(auto_now_add=True)
    temperatura = models.IntegerField(blank=False,verbose_name="Temperatura")

    def __str__(self):
        return self.dia_e_hora.strftime('%d/%m/%Y %H:%M:%S')

    class Meta:
        verbose_name = "Dados Produção Machine 1"
        verbose_name_plural = "Produção Machine 1"
