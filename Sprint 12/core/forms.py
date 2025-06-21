# core/forms.py
from django import forms
from .models import Propietario, Mascota, Cita

class PropietarioForm(forms.ModelForm):
    class Meta: model, fields = Propietario, "__all__"

class MascotaForm(forms.ModelForm):
    class Meta: model, fields = Mascota, "__all__"

class CitaForm(forms.ModelForm):
    class Meta: model, fields = Cita, "__all__"
