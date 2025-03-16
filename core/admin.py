from django.contrib import admin
from django.db import models
from core.models import EstadoBotao
# Register your models here.
class EstadoBotaoAdmin(admin.ModelAdmin):
    pass


admin.site.register(EstadoBotao, EstadoBotaoAdmin)
