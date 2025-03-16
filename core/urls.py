from django.urls import path
from .views import EstadoCreateView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('novodado/', EstadoCreateView.as_view(), name='create_estado'),
]
