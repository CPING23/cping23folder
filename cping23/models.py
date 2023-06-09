from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    goles_local = models.PositiveIntegerField()
    goles_visitante = models.PositiveIntegerField()



class TablaPosiciones(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    puntos = models.PositiveIntegerField(default=0)
    partidos_jugados = models.PositiveIntegerField(default=0)
    partidos_ganados = models.PositiveIntegerField(default=0)
    partidos_empatados = models.PositiveIntegerField(default=0)
    partidos_perdidos = models.PositiveIntegerField(default=0)
    goles_favor = models.PositiveIntegerField(default=0)
    goles_contra = models.PositiveIntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)

    @staticmethod
    def calcular_posiciones():
        equipos = Equipo.objects.all()
        TablaPosiciones.objects.all().delete()

        for equipo in equipos:
            partidos_local = Partido.objects.filter(equipo_local=equipo)
            partidos_visitante = Partido.objects.filter(equipo_visitante=equipo)
            partidos_jugados = partidos_local.count() + partidos_visitante.count()

            partidos_ganados = partidos_local.filter(goles_local__gt=models.F('goles_visitante')).count()
            partidos_ganados += partidos_visitante.filter(goles_visitante__gt=models.F('goles_local')).count()

            partidos_empatados = partidos_local.filter(goles_local=models.F('goles_visitante')).count()
            partidos_empatados += partidos_visitante.filter(goles_visitante=models.F('goles_local')).count()

            partidos_perdidos = partidos_jugados - partidos_ganados - partidos_empatados

            goles_favor = partidos_local.aggregate(total=models.Sum('goles_local'))['total'] or 0
            goles_favor += partidos_visitante.aggregate(total=models.Sum('goles_visitante'))['total'] or 0

            goles_contra = partidos_local.aggregate(total=models.Sum('goles_visitante'))['total'] or 0
            goles_contra += partidos_visitante.aggregate(total=models.Sum('goles_local'))['total'] or 0

            puntos = partidos_ganados * 3 + partidos_empatados

            diferencia_goles = goles_favor - goles_contra

            TablaPosiciones.objects.create(
                equipo=equipo,
                puntos=puntos,
                partidos_jugados=partidos_jugados,
                partidos_ganados=partidos_ganados,
                partidos_empatados=partidos_empatados,
                partidos_perdidos=partidos_perdidos,
                goles_favor=goles_favor,
                goles_contra=goles_contra,
                diferencia_goles=diferencia_goles
            )

@receiver(post_save, sender=Partido)
def actualizar_tabla_posiciones(sender, instance, **kwargs):
    TablaPosiciones.calcular_posiciones()