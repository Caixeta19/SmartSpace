from django.contrib import admin
from .models import AgendamentoCancelado, Sala, Agendamento

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade')
    search_fields = ('nome',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('sala', 'usuario', 'data', 'horario_inicio', 'horario_fim')
    list_filter = ('sala', 'data')
    search_fields = ('usuario__username', 'sala__nome')
    
@admin.register(AgendamentoCancelado)
class AgendamentoCanceladoAdmin(admin.ModelAdmin):
    list_display = ('sala', 'data', 'hora_inicio', 'hora_fim', 'motivo', 'solicitante', 'data_cancelamento')
    list_filter = ('sala', 'data_cancelamento')
    search_fields = ('motivo',)
