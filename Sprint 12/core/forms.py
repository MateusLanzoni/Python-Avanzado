# core/forms.py
from django import forms
from .models import Propietario, Mascota, Cita
from django.forms import DateInput

class PropietarioForm(forms.ModelForm):
    class Meta: 
        model = Propietario
        fields = "__all__"

class MascotaForm(forms.ModelForm):
    class Meta: 
        model = Mascota
        fields = "__all__"

class CitaForm(forms.ModelForm):
    fecha = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=DateInput(format="%d/%m/%Y", attrs={"placeholder": "DD/MM/AAAA"})
    )
    class Meta:
        model = Cita
        fields = "__all__"