# forms.py
from django import forms
from .models import EstadoBotao


class CreateEstadoForm(forms.ModelForm):
    horario = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Preencha o horario', 'class': 'form-control'}
        ))
    estado = forms.IntegerField()

    class Meta:
        model = EstadoBotao
        fields = ['horario', 'estado']
