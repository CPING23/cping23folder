from django.shortcuts import render, get_object_or_404
from .models import Equipo, TablaPosiciones, Partido, Evento

def tabla_posiciones(request):
    posiciones = TablaPosiciones.objects.order_by('-puntos', '-goles_favor')

    context = {
        'posiciones': posiciones
    }

    return render(request, 'tabla_posiciones.html', context)

def lista_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'partidos.html', {'partidos': partidos})


def resumen(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    partidos = Partido.objects.all()
    eventos = Evento.objects.all()
    context = {
        'partido': partido,
        'partidos': partidos,
        'eventos': eventos
    }
    return render(request, 'resumen.html', context)
