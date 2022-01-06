from django.http import HttpResponse
import urllib.request
from bs4 import BeautifulSoup
from .serializers import VacinaSerializer, PessoaSerializer, NotificacaoSerializer
from rest_framework import viewsets, permissions
from .models import Vacina, Pessoa, Notificacao


def index(request):
    html = urllib.request.urlopen("https://vacinacovid.saobernardo.sp.gov.br/VacinaSBCProd/servlet/inicial")
    bs = BeautifulSoup(html, 'html.parser')
    buscar_faixas(3, bs)
    return HttpResponse("Validação do Django em app.vacina")


def buscar_faixas(dose_final, bs):
    for dose in range(1, dose_final + 1):
        id_select = f"vPUBLICOALVOVACINAID_D{dose}"
        select = bs.find('select', id=id_select)
        options = select.find_all('option')
        print(f"Vacinação Dose{dose}")
        for option in options:
            if option['value'] != "":
                print(f"ID: {option['value']} DESCRIÇÃO: {option.text}")
        print("*******************")


class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer
    permission_classes = [permissions.IsAuthenticated]


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    permission_classes = [permissions.IsAuthenticated]
