from django.conf import settings
from confluent_kafka import Producer
import json

# Configuración del productor Kafka
producer = Producer({
    'bootstrap.servers': '127.0.0.1:9092',   # fuerza IPv4 en Windows
    'broker.address.family': 'v4'            # evita intentos en IPv6
})

def enviar_evento_calificacion(calificacion):
    """
    Envía un evento de calificación al tópico Kafka 'calificaciones'.
    """

    # Si Kafka está desactivado en modo DEBUG/test, no enviar nada
    if not getattr(settings, "KAFKA_ENABLED", True):
        return

    # Tomar todos los factores asociados (usando related_name="factores")
    factores = [
        {
            "numero_factor": f.numero_factor,
            "valor_factor": float(f.valor_factor),
        }
        for f in calificacion.factores.all()
    ]

    # Construir payload con calificación + factores
    data = {
        "id_calificacion": calificacion.id_calificacion,   # 👉 consistente con EventoKafka
        "instrumento": calificacion.instrumento,
        "descripcion": calificacion.descripcion,
        "fecha_pago": str(calificacion.fecha_pago),
        "valor_historico": float(calificacion.valor_historico),
        "factores": factores,
    }

    # Enviar al tópico Kafka
    producer.produce(
        topic='calificaciones',
        value=json.dumps(data).encode('utf-8')
    )

    # Forzar envío inmediato (útil en modo síncrono)
    producer.flush()
