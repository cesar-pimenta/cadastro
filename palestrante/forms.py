from django.forms import ModelForm
from .models import *

class PalestranteForm(ModelForm):
    class Meta:
        model = Palestrante
        fields = [

            'tema', 'palestrante', 'cargo', 'resumo', 'email', 'telefone',

        ]