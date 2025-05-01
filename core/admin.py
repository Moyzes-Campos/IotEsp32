from django.contrib import admin
from django.db import models
from core.models import EstadoBotao, TesteRest
# Register your models here.
class EstadoBotaoAdmin(admin.ModelAdmin):
    pass

class TemperaturasAdmin(admin.ModelAdmin):
    pass


admin.site.register(EstadoBotao, EstadoBotaoAdmin)
admin.site.register(TesteRest, TemperaturasAdmin)
