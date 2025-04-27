from django.db import models
from django.shortcuts import reverse


# Create your models here.
class EstadoBotao(models.Model):
    jsonfield = models.JSONField()

    def get_absolute_url(self):
        return reverse('index')
