# miapp/views_monitor.py
from django.http import HttpResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

# Métricas personalizadas
login_counter = Counter('login_total', 'Número total de logins exitosos')
calificacion_creada_counter = Counter('calificacion_creada_total', 'Número de calificaciones creadas')
calificacion_actualizada_counter = Counter('calificacion_actualizada_total', 'Número de calificaciones actualizadas')
calificacion_importada_counter = Counter('calificacion_importada_total', 'Número de calificaciones importadas')

def metrics_view(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)
