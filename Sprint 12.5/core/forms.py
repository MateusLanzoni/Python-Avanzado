# core/forms.py
from django import forms
from .models import Propietario, Mascota, Cita, Medicamento, Veterinario, Cirugia, BitacoraConsulta
from django.forms import DateInput, DateTimeInput

class PropietarioForm(forms.ModelForm):
    class Meta: 
        model, fields = Propietario, "__all__"

class MascotaForm(forms.ModelForm):
    class Meta: 
        model, fields = Mascota, "__all__"

class CitaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    class Meta:
        model = Cita
        fields = "__all__"


class MedicamentoForm(forms.ModelForm):
    fecha_vencimiento = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    
    class Meta:
        model = Medicamento
        fields = ['nombre', 'descripcion', 'cantidad_disponible', 'fecha_vencimiento']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }


class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'especialidad', 'telefono']


class CirugiaForm(forms.ModelForm):
    fecha = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"})
    )
    
    class Meta:
        model = Cirugia
        fields = ['fecha', 'tipo_cirugia', 'descripcion', 'estado', 'mascota', 'veterinario']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }


class BitacoraConsultaForm(forms.ModelForm):
    class Meta:
        model = BitacoraConsulta
        fields = ['mascota', 'veterinario', 'observaciones', 'diagnostico', 'tratamiento', 
                 'medicamentos_recetados', 'peso', 'temperatura']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'rows': 3}),
            'medicamentos_recetados': forms.CheckboxSelectMultiple(),
            'peso': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'kg'}),
            'temperatura': forms.NumberInput(attrs={'step': '0.1', 'placeholder': '°C'}),
        }
