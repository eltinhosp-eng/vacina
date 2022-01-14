from django.contrib import admin

from .models import Vacina, Pessoa, Notificacao

admin.site.register(Vacina)

admin.site.register(Pessoa)

admin.site.register(Notificacao)
