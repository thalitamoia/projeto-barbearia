from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.http import HttpResponse
from weasyprint import HTML 
from django.template.loader import render_to_string

# Create your views here.
def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agendar.html', {'form': form})


def ver_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'ver_agendamentos.html', {'agendamentos': agendamentos})


def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('ver_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agendar.html', {'form': form, 'edit': True})

def excluir_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('ver_agendamentos')
    return render(request, 'confirmar_exclusao.html', {'agendamento': agendamento})

def gerar_fatura_pdf(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    html_string = render_to_string('fatura.html', {'agendamento': agendamento})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=fatura_{agendamento.nome}.pdf'
    return response