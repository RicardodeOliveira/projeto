from django.forms import ModelForm
from .models import Lancamento

class CteForm(ModelForm):
    class Meta:
        model = Lancamento
        fields = ['cte', 'cliente', 'estado', 'cidade', 'emissao', 'peso', 'frete']