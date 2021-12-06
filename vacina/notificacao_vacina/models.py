from django.db import models


# Create your models here.
class Vacina(models.Model):
    descricao = models.CharField(max_length=200)
    codigo = models.IntegerField(default=0)
    dose = models.IntegerField(default=0)

