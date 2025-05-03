from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import EstadoBotao, ProducaoMachine1, SetupMachine1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProducaoMachine1Serializer, SetupMachine1Serializer
from django.db.models import Count, Avg

# Create your views here.
from .forms import CreateEstadoForm


@method_decorator(csrf_exempt, name='dispatch')
class EstadoCreateView(CreateView):
    model = EstadoBotao
    template_name = 'core/add_estadobotao.html'
    form_class = CreateEstadoForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        dados_agrupados = (
            ProducaoMachine1.objects.values('dia').annotate(
                total_registros=Count('id'),
                media_temperatura=Avg('temperatura')
            )
            .order_by('-dia'))
        context['dados'] = dados_agrupados
        context['production'] = ProducaoMachine1.objects.all()
        return context


class ProducaoMachine1View(APIView):
    def get(self, request):
        temperatura = ProducaoMachine1.objects.all()
        serializer = ProducaoMachine1Serializer(temperatura, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProducaoMachine1Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SetupMachine1View(APIView):
    def get(self, request):
        try:
            ultimo = SetupMachine1.objects.first()  # usa ordering para pegar o mais novo
        except SetupMachine1.DoesNotExist:
            return Response({"detail": "Nenhum dado encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SetupMachine1Serializer(ultimo)
        return Response(serializer.data)
