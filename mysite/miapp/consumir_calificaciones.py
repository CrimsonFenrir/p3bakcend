from django.core.management.base import BaseCommand
from confluent_kafka import Consumer
import json
from miapp.models import Calificacion, CalificacionFactor, EventoKafka

class Command(BaseCommand):
    help = "Consume eventos de calificaciones desde Kafka"

    def handle(self, *args, **options):
        consumer = Consumer({
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'miapp-group',
            'auto.offset.reset': 'earliest'
        })

        consumer.subscribe(['calificaciones'])

        self.stdout.write(self.style.SUCCESS("Esperando mensajes de Kafka..."))

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    self.stderr.write(f"Error en Kafka: {msg.error()}")
                    continue

                data = json.loads(msg.value().decode('utf-8'))

                # Guardar evento crudo en tabla EventoKafka
                evento = EventoKafka.objects.create(
                    id_calificacion=data.get("id"),
                    instrumento=data.get("instrumento"),
                    descripcion=data.get("descripcion"),
                    fecha_pago=data.get("fecha_pago"),
                    valor_historico=data.get("valor_historico"),
                )

                # Crear o actualizar la calificación principal
                cal, created = Calificacion.objects.update_or_create(
                    id_calificacion=data.get("id"),
                    defaults={
                        "instrumento": data.get("instrumento"),
                        "descripcion": data.get("descripcion"),
                        "fecha_pago": data.get("fecha_pago"),
                        "valor_historico": data.get("valor_historico"),
                    }
                )

                # Guardar factores asociados
                factores = data.get("factores", [])
                for f in factores:
                    CalificacionFactor.objects.update_or_create(
                        calificacion=cal,
                        numero_factor=f.get("numero_factor"),
                        defaults={"valor_factor": f.get("valor_factor")}
                    )

                self.stdout.write(self.style.SUCCESS(
                    f"Procesado evento de calificación {cal.id_calificacion} con {len(factores)} factores"
                ))

        except KeyboardInterrupt:
            self.stdout.write("Consumidor detenido manualmente.")
        finally:
            consumer.close()
