from rest_framework import viewsets
from .models import Calificacion, CalificacionFactor
from .serializers import CalificacionSerializer, CalificacionFactorSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.prefetch_related('factores').all()
    serializer_class = CalificacionSerializer

class CalificacionFactorViewSet(viewsets.ModelViewSet):
    queryset = CalificacionFactor.objects.all()
    serializer_class = CalificacionFactorSerializer
