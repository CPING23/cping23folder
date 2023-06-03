from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(Gol_local)
admin.site.register(Evento)
admin.site.register(Evento_redcard_local)
admin.site.register(Evento_redcard_visitante)
admin.site.register(Evento_yllwcard_local)
admin.site.register(Evento_yllwcard_visitante)
admin.site.register(Evento_gol_local)
admin.site.register(Evento_gol_visitante)
admin.site.register(Evento_cambio_local)
admin.site.register(Evento_cambio_visitante)
admin.site.register(Gol_visitante)
admin.site.register(Tarjetaroja_local)
admin.site.register(Tarjetaroja_visitante)
admin.site.register(Tarjetaamarilla_local)
admin.site.register(TablaPosiciones)