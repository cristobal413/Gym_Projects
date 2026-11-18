from django import forms
from .models import ProductoGym


class ProductoGymForm(forms.ModelForm):
    class Meta:
        model = ProductoGym
        fields = [
            'categoria',
            'nombre',
            'marca',
            'precio_clp',
            'stock',
            'fecha_ingreso',
            'disponible',
            'imagen',
        ]
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Mancuernas Hexagonales 10kg'
            }),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Everlast / Rogue / Genérica'
            }),
            'precio_clp': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 25000'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 15'
            }),
            'fecha_ingreso': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }