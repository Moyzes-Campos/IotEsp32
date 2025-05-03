from rest_framework import serializers
from .models import ProducaoMachine1, SetupMachine1


class ProducaoMachine1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProducaoMachine1
        fields = [
            'id',
            'dia',
            'dia_e_hora',
            'temperatura'
        ]


class SetupMachine1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SetupMachine1
        fields = [
            'id',
            'temperatura_setup_le',
            'tempo_setup_le',
            'temperatura_setup_ld',
            'tempo_setup_ld',
            'criado'
        ]
