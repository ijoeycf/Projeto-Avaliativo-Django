
from django import forms
from .models import Agendamento


class AgendamentoForm(forms.ModelForm):

    dataAgendada = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            },
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Agendamento

        fields = [
            'nomeCliente',
            'preco',
            'servico',
            'dataAgendada',
        ]

        labels = {
            'nomeCliente': 'Nome da cliente',
            'preco': 'Valor do serviço (R$)',
            'servico': 'Descrição do serviço',
            'dataAgendada': 'Data e horário do agendamento',
        }

        