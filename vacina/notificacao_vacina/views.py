from django.http import HttpResponse


def index(request):
    return HttpResponse("Validação do Django em app.vacina")
