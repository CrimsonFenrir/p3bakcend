from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    instrumento = models.CharField(max_length=50, verbose_name="Instrumento")
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")
    fecha_pago = models.DateField(null=True, blank=True, verbose_name="Fecha de pago")
    valor_historico = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(0)], verbose_name="Valor histórico"
    )

    class Meta:
        db_table = 'CALIFICACION'
        indexes = [
            models.Index(fields=['instrumento']),
            models.Index(fields=['fecha_pago']),
        ]

    def __str__(self):
        return f"{self.instrumento} - {self.descripcion or 'Sin descripción'}"


class CalificacionFactor(models.Model):
    id_factor = models.AutoField(primary_key=True)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE, related_name="factores")
    numero_factor = models.IntegerField(
        validators=[MinValueValidator(8), MaxValueValidator(38)],
        verbose_name="Número de factor"
    )
    valor_factor = models.DecimalField(
        max_digits=10, decimal_places=8, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        verbose_name="Valor del factor"
    )

    class Meta:
        db_table = 'CALIFICACION_FACTOR'
        unique_together = ('calificacion', 'numero_factor')
        indexes = [
            models.Index(fields=['calificacion']),
            models.Index(fields=['numero_factor']),
        ]

    def __str__(self):
        return f"Factor {self.numero_factor} = {self.valor_factor:.4f}"

class EventoKafka(models.Model):
    id_calificacion = models.IntegerField()
    instrumento = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank=True)
    valor_historico = models.DecimalField(max_digits=20, decimal_places=2)
    recibido_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EventoKafka {self.id_calificacion} - {self.instrumento}"
