from django import forms

from .models import Servicio


class ServicioForm(forms.ModelForm):
    """
    Formulario del módulo Servicios. Define qué campos se piden
    y cómo se validan (30% de la evidencia: formularios HTML
    procesados en el servidor).
    """

    class Meta:
        model = Servicio
        fields = [
            'nombre',
            'descripcion',
            'categoria',
            'duracion_minutos',
            'precio',
            'popular',
            'activo',
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ej. Corte y estilo'}
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Describe brevemente el servicio',
                }
            ),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'duracion_minutos': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 5}
            ),
            'precio': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 0, 'step': '0.01'}
            ),
            'popular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nombre': 'Nombre del servicio',
            'descripcion': 'Descripción',
            'categoria': 'Categoría',
            'duracion_minutos': 'Duración (minutos)',
            'precio': 'Precio (COP)',
            'popular': '¿Servicio popular?',
            'activo': '¿Servicio activo?',
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre del servicio debe tener al menos 3 caracteres.'
            )
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a cero.')
        return precio

    def clean_duracion_minutos(self):
        duracion = self.cleaned_data['duracion_minutos']
        if duracion <= 0:
            raise forms.ValidationError(
                'La duración debe ser mayor a cero minutos.'
            )
        return duracion
