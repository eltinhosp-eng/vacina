from rest_framework import serializers
from models import Vacina, Pessoa, Notificacao


class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = [
            'descricao',
            'codigo',
            'dose',
        ]


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'celular',
            'email',
        ]


class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = [
            'pessoa',
            'vacina',
            'notificacao_celular',
            'notificacao_email',
        ]
