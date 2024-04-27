# En events/forms.py
from django import forms
from .models import Evento, RegistroEvento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = '__all__'
