from django.forms import ModelForm
from .models import Transacao


class TransacaoFormulario(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']
