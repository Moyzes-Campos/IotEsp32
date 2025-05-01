from django.urls import path
from .views import EstadoCreateView, IndexView, ProducaoMachine1View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('novodado/', EstadoCreateView.as_view(), name='create_estado'),
    path('temperaturas/', ProducaoMachine1View.as_view(), name='machine1')
]
