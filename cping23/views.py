from django.shortcuts import render
from .models import Equipo, TablaPosiciones, Partido

def tabla_posiciones(request):
    posiciones = TablaPosiciones.objects.order_by('-puntos', '-goles_favor')

    context = {
        'posiciones': posiciones
    }

    return render(request, 'tabla_posiciones.html', context)

def lista_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'partidos.html', {'partidos': partidos})


