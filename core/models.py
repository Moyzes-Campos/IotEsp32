from django.db import models
from django.shortcuts import reverse


# Create your models here.
class EstadoBotao(models.Model):
    jsonfield = models.JSONField()

    def get_absolute_url(self):
        return reverse('index')


class TesteRest(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    temperatura = models.IntegerField(blank=False,verbose_name="Tempêratura")
