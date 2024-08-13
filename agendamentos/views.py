from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# Create your views here.
def index(request):
    return render(request,'index.html')


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

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="fatura_{agendamento.nome}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.drawString(100, height - 100, f"Nome: {agendamento.nome}")
    p.drawString(100, height - 120, f"Telefone: {agendamento.telefone}")
    p.drawString(100, height - 140, f"Email: {agendamento.email}")
    p.drawString(100, height - 160, f"Data: {agendamento.data}")
    p.drawString(100, height - 180, f"Horário: {agendamento.horario}")
    p.drawString(100, height - 200, f"Serviço: {agendamento.servico}")
    p.drawString(100, height - 220, f"Valor: R$ {agendamento.valor}")
    p.drawString(100, height - 240, f"Contribuinte: {'Sim' if agendamento.contribuinte else 'Não'}")
    if agendamento.contribuinte:
        p.drawString(100, height - 260, f"Número do Contribuinte: {agendamento.contribuinte_numero}")
    p.drawString(100, height - 280, f"Observações: {agendamento.observacao}")

    p.showPage()
    p.save()

    return response
