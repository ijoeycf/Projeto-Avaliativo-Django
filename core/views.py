from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Agendamento
from .forms import AgendamentoForm



def home(request):
    return render(request, 'index.html')





def agendamentos(request):
    agendamentos = Agendamento.objects.all()

    return render(request, 'agendamentos.html', {
        'agendamentos': agendamentos
    })





def cadastraAgendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('agendamentos')
    else:
        form = AgendamentoForm()

    return render(request, 'formulario.html', {'form': form})





def editaAgendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)

        if form.is_valid():
            form.save()
            return redirect('agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, 'formulario.html', {'form': form})


@require_POST
def excluiAgendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.delete()
    return redirect('agendamentos')