from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import EstadoBotao

# Create your views here.
from .forms import CreateEstadoForm


@ensure_csrf_cookie
class EstadoCreateView(CreateView):
    model = EstadoBotao
    template_name = 'core/add_estadobotao.html'
    form_class = CreateEstadoForm


class IndexView(TemplateView):
    template_name = 'index.html'
