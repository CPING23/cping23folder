from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(Gol_local)
admin.site.register(Gol_visitante)
admin.site.register(Tarjetaroja_local)
admin.site.register(Tarjetaroja_visitante)
admin.site.register(Tarjetaamarilla)
admin.site.register(TablaPosiciones)