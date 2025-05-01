from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import EstadoBotao, TesteRest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TesteRestSerializer


# Create your views here.
from .forms import CreateEstadoForm


@method_decorator(csrf_exempt, name='dispatch')
class EstadoCreateView(CreateView):
    model = EstadoBotao
    template_name = 'core/add_estadobotao.html'
    form_class = CreateEstadoForm


class IndexView(TemplateView):
    template_name = 'index.html'


class TesteRestView(APIView):
    def get(self, request):
        temperatura = TesteRest.objects.all()
        serializer = TesteRestSerializer(temperatura, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TesteRestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)