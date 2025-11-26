from rest_framework import serializers
from .models import Calificacion, CalificacionFactor

class CalificacionFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionFactor
        fields = ['id', 'numero_factor', 'valor_factor']

class CalificacionSerializer(serializers.ModelSerializer):
    factores = CalificacionFactorSerializer(many=True, read_only=True)

    class Meta:
        model = Calificacion
        fields = ['id_calificacion', 'instrumento', 'descripcion', 'fecha_pago', 'valor_historico', 'factores']
