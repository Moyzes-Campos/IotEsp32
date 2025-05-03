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


class SetupMachine1(models.Model):
    temperatura_setup_le = models.DecimalField(decimal_places=2, max_digits=5, help_text="Celcius")
    tempo_setup_le = models.DecimalField(decimal_places=2, max_digits=5, help_text="Segundos")
    temperatura_setup_ld = models.DecimalField(decimal_places=2, max_digits=5)
    tempo_setup_ld = models.DecimalField(decimal_places=2, max_digits=5)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.criado.strftime('%d/%m/%Y %H:%M:%S')

    class Meta:
        verbose_name = "Setup Machine 1"
        verbose_name_plural = "Setup Machine 1"
        ordering = ['-criado']
