from django.contrib import admin
from django.db import models
from core.models import EstadoBotao, ProducaoMachine1
# Register your models here.


class Machine1Admin(admin.ModelAdmin):
    pass


admin.site.register(ProducaoMachine1, Machine1Admin)
