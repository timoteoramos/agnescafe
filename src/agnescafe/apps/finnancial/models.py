from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class CashFlow(SoftDeletableModel, TimeStampedModel):
    description = models.CharField(
        max_length=64,
        verbose_name="descrição",
    )

    input = models.BooleanField(
        default=True,
        verbose_name="entrada",
    )

    total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="total",
    )

    def __str__(self):
        return f"{self.created} {"Entrada" if self.input else "Saída"}: R$ {self.total}"

    class Meta:
        verbose_name = "fluxo de caixa"
        verbose_name_plural = "fluxos de caixa"
