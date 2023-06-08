
from django.shortcuts import render, get_object_or_404
from .models import Equipo, TablaPosiciones, Partido, Evento, EventoPartido

def tabla_posiciones(request):
    TablaPosiciones.calcular_posiciones()
    posiciones = TablaPosiciones.objects.order_by('-puntos', '-goles_favor')

    context = {
        'posiciones': posiciones
    }

    return render(request, 'tabla_posiciones.html', context)



def mostrar_partidos(request):
    deporte = request.GET.get('deporte', 'FUTBOL_MASCULINO')  # Valor por defecto: Fútbol Masculino
    partidos = Partido.objects.filter(deporte=deporte)
    return render(request, 'partidos.html', {'partidos': partidos})

def resumen(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    partidos = Partido.objects.all()
    eventos_partido = EventoPartido.objects.filter(partido=partido)
    eventos = Evento.objects.filter(partido=partido)

    context = {
        'partido': partido,
        'partidos': partidos,
        'eventos_partido': eventos_partido,
        'eventos': eventos
    }

    return render(request, 'resumen.html', context)

