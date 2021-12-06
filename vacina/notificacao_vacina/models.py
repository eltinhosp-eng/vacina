from django.db import models


# Create your models here.
class Vacina(models.Model):
    descricao = models.CharField(max_length=200)
    codigo = models.IntegerField(default=0)
    dose = models.IntegerField(default=0)


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=50)


class Notificacao(models.Model):
    RESPOSTAS = (
        ('S', 'Sim'),
        ('N', 'Não')
    )
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    notificacao_celular = models.CharField(max_length=1, choices=RESPOSTAS)
    notificacao_email = models.CharField(max_length=1, choices=RESPOSTAS)

