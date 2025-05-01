from rest_framework import serializers
from .models import TesteRest


class TesteRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesteRest
        fields = [
            'id',
            'criado',
            'modificado',
            'temperatura'
        ]

