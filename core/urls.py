from django.urls import path
from .views import EstadoCreateView, IndexView, ProducaoMachine1View, SetupMachine1View, MonitoramentoIndexView, MonitoramentoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('novodado/', EstadoCreateView.as_view(), name='create_estado'),
    path('temperaturas/', ProducaoMachine1View.as_view(), name='machine1'),
    path('setupmachine1/', SetupMachine1View.as_view(), name='setup_machine1'),
    path('monitoramento/', MonitoramentoIndexView.as_view(), name='monitoramento'),
    path('monitoramento_add/', MonitoramentoView.as_view(), name='monitoramento_add')
]
