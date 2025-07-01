from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Sala(models.Model):
    nome = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    imagem = models.ImageField(upload_to='salas_imagens/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def clean(self):
        # Verifica conflitos de horário para a mesma sala
        conflitos = Agendamento.objects.filter(
            sala=self.sala,
            data=self.data,
        ).exclude(id=self.id)

        for agendamento in conflitos:
            if (
                self.horario_inicio < agendamento.horario_fim
                and self.horario_fim > agendamento.horario_inicio
            ):
                raise ValidationError(
                    f"A sala '{self.sala.nome}' já está ocupada entre {agendamento.horario_inicio} e {agendamento.horario_fim}."
                )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sala.nome} - {self.data} ({self.horario_inicio} - {self.horario_fim})"


class AgendamentoCancelado(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    motivo = models.TextField()
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_cancelamento = models.DateTimeField(auto_now_add=True)

