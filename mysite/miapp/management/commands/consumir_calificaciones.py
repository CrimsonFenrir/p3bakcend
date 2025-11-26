from django.core.management.base import BaseCommand
from confluent_kafka import Consumer
import json
import logging
from django.core.mail import send_mail
from miapp.models import EventoKafka
from datetime import datetime

logger = logging.getLogger('miapp')

class Command(BaseCommand):
    help = "Consume eventos de calificaciones desde Kafka"

    def handle(self, *args, **options):
        consumer_conf = {
            'bootstrap.servers': '127.0.0.1:9092',
            'broker.address.family': 'v4',
            'group.id': 'miapp-consumidor',
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(consumer_conf)
        consumer.subscribe(['calificaciones'])

        self.stdout.write(self.style.SUCCESS("📡 Consumidor Kafka iniciado..."))

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    logger.error(f"Error en Kafka: {msg.error()}")
                    continue

                # Decodificar mensaje
                data = json.loads(msg.value().decode('utf-8'))
                logger.info(f"📩 Evento recibido: {data}")

                # Guardar en BD
                try:
                    fecha_pago = data.get("fecha_pago")
                    if fecha_pago:
                        try:
                            fecha_pago = datetime.fromisoformat(fecha_pago)
                        except Exception:
                            pass  # deja la cadena si no es ISO

                    EventoKafka.objects.create(
                        id_calificacion=data.get("id_calificacion"),
                        instrumento=data.get("instrumento"),
                        descripcion=data.get("descripcion"),
                        fecha_pago=fecha_pago,
                        valor_historico=data.get("valor_historico"),
                    )
                    logger.info("Evento guardado en BD")
                except Exception as e:
                    logger.error(f"Error guardando evento en BD: {e}")

                # Enviar correo de alerta
                try:
                    mensaje = f"Se recibió una nueva calificación:\n{data}"
                    send_mail(
                        subject="📩 Nueva Calificación en Kafka",
                        message=mensaje,
                        from_email="alertas@tu-sitio.com",
                        recipient_list=["equipo@tu-sitio.com"],
                        fail_silently=True,
                    )
                    logger.info("Correo de alerta enviado")
                except Exception as e:
                    logger.error(f"Error enviando correo: {e}")

                self.stdout.write(self.style.SUCCESS(f"Procesado evento: {data}"))

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Consumidor detenido manualmente"))
        finally:
            consumer.close()
