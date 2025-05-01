from rest_framework import serializers
from .models import ProducaoMachine1


class ProducaoMachine1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProducaoMachine1
        fields = [
            'id',
            'criado',
            'modificado',
            'temperatura'
        ]

