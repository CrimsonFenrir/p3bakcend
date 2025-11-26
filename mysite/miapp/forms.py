from django import forms
from django.core.exceptions import ValidationError
from .models import Calificacion, CalificacionFactor
import datetime

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['instrumento', 'descripcion', 'fecha_pago', 'valor_historico']

    def clean_fecha_pago(self):
        fecha = self.cleaned_data.get('fecha_pago')
        if fecha and fecha > datetime.date.today():
            raise ValidationError("La fecha de pago no puede ser futura.")
        return fecha


class CalificacionFactorForm(forms.ModelForm):
    class Meta:
        model = CalificacionFactor
        fields = ['numero_factor', 'valor_factor']
        widgets = {
            # El número de factor se muestra pero no se puede editar
            'numero_factor': forms.NumberInput(attrs={'readonly': 'readonly'})
        }

    def clean(self):
        cleaned_data = super().clean()
        numero = cleaned_data.get('numero_factor')
        valor = cleaned_data.get('valor_factor')
        # Si ambos están vacíos, no marcar error (factor opcional)
        if numero is None and valor is None:
            self._errors.clear()
        return cleaned_data


class ExcelUploadForm(forms.Form):
    archivo = forms.FileField(label="Archivo Excel (.xlsx)")
