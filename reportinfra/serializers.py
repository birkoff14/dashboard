from rest_framework import serializers
from .models import actividades
class actividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = actividades
        fields = ["TipoActividad", "FechaInicio", "FechaFin", "Usuario", "Ambiente"], 