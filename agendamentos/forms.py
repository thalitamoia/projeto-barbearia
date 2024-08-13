from django import forms
from .models import Agendamento


from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'telefone', 'email', 'data', 'horario', 'servico', 'valor', 'observacao', 'contribuinte', 'contribuinte_numero']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }
