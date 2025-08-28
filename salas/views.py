from django.shortcuts import render, get_object_or_404, redirect
from .models import AgendamentoCancelado, Sala, Agendamento, User
from .forms import AgendamentoForm
from .models import Agendamento
from django.contrib.auth.decorators import login_required
from .utils import exportar_csv
from . import views


@login_required
def listar_salas(request):
    salas = Sala.objects.all()
    return render(request, 'salas/listar_salas.html', {'salas': salas})

@login_required
def detalhes_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    agendamentos = sala.agendamento_set.all()  # Agendamentos relacionados à sala
    return render(request, 'salas/agendar_sala.html', {'sala': sala, 'agendamentos': agendamentos})

@login_required
def agendar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)  # Buscar a sala pelo ID

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.sala = sala  # Associar o agendamento à sala
            agendamento.save()  # Salvar o agendamento no banco de dados
            return redirect('listar_salas')  # Redireciona para a lista de salas
    else:
        form = AgendamentoForm()

    return render(request, 'salas/agendar_sala.html', {'form': form, 'sala': sala})
@login_required
def listar_agendamentos(request):
    """
    Lista todos os agendamentos ordenados por data e horário de início.
    """
    agendamentos = Agendamento.objects.select_related('sala').order_by('data', 'horario_inicio')
    return render(request, 'salas/listar_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def listar_meus_agendamentos(request):
    """
    Lista apenas os agendamentos do usuário autenticado.
    """
    if request.user.is_authenticated:  # Verifica se o usuário está logado
        agendamentos = Agendamento.objects.filter(
            usuario=request.user  # Filtra pelos agendamentos do usuário logado
        ).select_related('sala').order_by('data', 'horario_inicio')
    else:
        agendamentos = []  # Se não estiver logado, retorna lista vazia
    
    return render(request, 'salas/listar_meus_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def editar_agendamento(request, pk):
    """
    Permite que o usuário edite um agendamento próprio.
    """
    agendamento = get_object_or_404(Agendamento, pk=pk, usuario=request.user)  # Garante que o usuário seja o dono
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('listar_meus_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'salas/editar_agendamento.html', {'form': form})

@login_required
def excluir_agendamento(request, pk):
    """
    Permite que o usuário exclua um agendamento próprio.
    """
    agendamento = get_object_or_404(Agendamento, pk=pk, usuario=request.user)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('listar_meus_agendamentos')
    return render(request, 'salas/confirmar_exclusao.html', {'agendamento': agendamento})

@login_required
def cancelar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk, usuario=request.user)

    if request.method == 'POST':
        motivo = request.POST.get('motivo')
        if motivo:
            # Cria o cancelamento
            AgendamentoCancelado.objects.create(
                sala=agendamento.sala,
                data=agendamento.data,
                hora_inicio=agendamento.horario_inicio,
                hora_fim=agendamento.horario_fim,
                motivo=motivo,
                solicitante=request.user,
            )
            agendamento.delete()  # Deleta o agendamento original
            return redirect('agendamentos_cancelados')

    # Renderiza a página de confirmação se for GET
    return render(request, 'salas/confirmar_exclusao.html', {'agendamento': agendamento})

@login_required
def listar_agendamentos_cancelados(request):
    cancelados = AgendamentoCancelado.objects.select_related('sala', 'solicitante').order_by('-data_cancelamento')
    return render(request, 'salas/listar_agendamentos_cancelados.html', {'cancelados': cancelados})

@login_required
def gerenciar_sala(request):
    if request.user.groups.filter(name="equipe").exists():
        return render(request, 'interno/gerenciar_salas.html')
    else:
        return redirect('homepage')

from django.http import HttpResponse
from .models import Sala, User, Agendamento, AgendamentoCancelado
from .utils import exportar_csv

@login_required(login_url='/usuarios/logar')
def exportar_relatorio(request, relatorio):
    if request.user.groups.filter(name="equipe").exists():
        if relatorio == "salas":
            info = Sala.objects.all()

        elif relatorio == "usuarios":
            info = User.objects.all()

        elif relatorio == "agendamentos":
            info = Agendamento.objects.all()

        elif relatorio == "cancelamentos":
            info = AgendamentoCancelado.objects.all()

        else:
            return HttpResponse("Relatório não encontrado", status=404)

        return exportar_csv(info, relatorio)

    return redirect('homepage')
