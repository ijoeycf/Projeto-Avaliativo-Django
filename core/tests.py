from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Agendamento


class EditaAgendamentoTests(TestCase):
    def setUp(self):
        self.agendamento = Agendamento.objects.create(
            nomeCliente='Cliente',
            preco='50.00',
            servico='Manicure',
            dataAgendada=timezone.now(),
        )

    def test_botao_alterar_abre_formulario_do_agendamento(self):
        response = self.client.get(reverse('agendamentos'))

        self.assertContains(
            response,
            reverse('editaAgendamento', args=[self.agendamento.id]),
        )

        response = self.client.get(
            reverse('editaAgendamento', args=[self.agendamento.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'value="Cliente"')

    def test_edita_agendamento_salva_dados(self):
        response = self.client.post(
            reverse('editaAgendamento', args=[self.agendamento.id]),
            {
                'nomeCliente': 'Cliente atualizado',
                'preco': '75.50',
                'servico': 'Pedicure',
                'dataAgendada': '2026-11-18 14:30:00',
            },
        )

        self.assertRedirects(response, reverse('agendamentos'))
        self.agendamento.refresh_from_db()
        self.assertEqual(self.agendamento.nomeCliente, 'Cliente atualizado')
        self.assertEqual(str(self.agendamento.preco), '75.50')
        self.assertEqual(self.agendamento.servico, 'Pedicure')


class ExcluiAgendamentoTests(TestCase):
    def setUp(self):
        self.agendamento = Agendamento.objects.create(
            nomeCliente='Cliente',
            preco='50.00',
            servico='Manicure',
            dataAgendada=timezone.now(),
        )

    def test_exclui_agendamento_e_redireciona_para_lista(self):
        response = self.client.post(
            reverse('excluiAgendamento', args=[self.agendamento.id])
        )

        self.assertRedirects(response, reverse('agendamentos'))
        self.assertFalse(
            Agendamento.objects.filter(id=self.agendamento.id).exists()
        )

    def test_exclusao_nao_aceita_get(self):
        response = self.client.get(
            reverse('excluiAgendamento', args=[self.agendamento.id])
        )

        self.assertEqual(response.status_code, 405)
        self.assertTrue(
            Agendamento.objects.filter(id=self.agendamento.id).exists()
        )
