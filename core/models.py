from django.db import models

# Create your models here.
class Agendamento(models.Model):
    nomeCliente = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    servico = models.TextField(max_length=100)
    dataAgendada = models.DateTimeField()
    dataCriacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nomeCliente