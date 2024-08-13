from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    email = models.EmailField()
    data = models.DateField()
    horario = models.TimeField()
    servico = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    contribuinte = models.BooleanField(default=False)
    contribuinte = models.BooleanField(default=False)
    contribuinte_numero = models.CharField(max_length=9, blank=True, null=True)

    def clean(self):
        if self.contribuinte and not self.contribuinte_numero:
            raise ValidationError('O número do contribuinte é obrigatório quando "Contribuinte" está marcado.')
        if self.contribuinte_numero and len(self.contribuinte_numero) != 9:
            raise ValidationError('O número do contribuinte deve ter exatamente 9 dígitos.')
        
    def __str__(self):
        return f"{self.nome} - {self.data} {self.horario}"