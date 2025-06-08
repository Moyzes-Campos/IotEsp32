from django.contrib import admin
from django.db import models
from core.models import EstadoBotao, ProducaoMachine1, SetupMachine1, MonitoramentoDunexa
# Register your models here.


class Machine1Admin(admin.ModelAdmin):
    pass


admin.site.register(ProducaoMachine1, Machine1Admin)


class SetupMachine1Admin(admin.ModelAdmin):
    pass


admin.site.register(SetupMachine1, SetupMachine1Admin)


class MonitoramentoAdmin(admin.ModelAdmin):
    pass


admin.site.register(MonitoramentoDunexa, MonitoramentoAdmin)
