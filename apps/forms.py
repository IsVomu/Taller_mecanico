from django import forms
from .models import Repuesto

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre', 'precio', 'fecha_ingreso', 'disponible', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }