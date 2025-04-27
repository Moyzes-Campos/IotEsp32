# forms.py
from django import forms
from .models import EstadoBotao


class CreateEstadoForm(forms.ModelForm):
    jsonfield = forms.JSONField()

    class Meta:
        model = EstadoBotao
        fields = ['jsonfield']
