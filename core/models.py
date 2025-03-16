from django.db import models
from django.shortcuts import reverse


# Create your models here.
class EstadoBotao(models.Model):
    horario = models.CharField(max_length=100)
    estado = models.IntegerField()

    def __str__(self):
        return self.horario

    def get_absolute_url(self):
        return reverse('index')
