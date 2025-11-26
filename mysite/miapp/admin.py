from django.contrib import admin
from .models import Calificacion,EventoKafka

@admin.register(EventoKafka)
class EventoKafkaAdmin(admin.ModelAdmin):
    list_display = (
        "id_calificacion",
        "instrumento",
        "descripcion",
        "fecha_pago",
        "valor_historico",
        "recibido_en",
    )
    list_filter = ("instrumento", "fecha_pago", "recibido_en")
    search_fields = ("id_calificacion", "instrumento", "descripcion")
    ordering = ("-recibido_en",)


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("id_calificacion", "instrumento", "descripcion", "fecha_pago", "valor_historico")
    list_filter = ("instrumento", "fecha_pago")
    search_fields = ("instrumento", "descripcion")
    ordering = ("-fecha_pago",)