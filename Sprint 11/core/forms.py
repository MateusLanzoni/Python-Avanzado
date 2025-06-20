from django import forms
from .models import Propietario, Mascota

class PropietarioForm(forms.ModelForm):
    class Meta:
        model  = Propietario
        fields = "__all__"

class MascotaForm(forms.ModelForm):
    class Meta:
        model  = Mascota
        fields = "__all__"