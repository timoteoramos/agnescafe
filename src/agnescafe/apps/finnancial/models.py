from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class PaymentMethod(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(
        max_length=32,
        verbose_name="nome",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "método de pagamento"
        verbose_name_plural = "métodos de pagamento"


class CashFlow(SoftDeletableModel, TimeStampedModel):
    description = models.CharField(
        max_length=64,
        verbose_name="descrição",
    )

    input = models.BooleanField(
        default=True,
        verbose_name="entrada",
    )

    payment_methods = models.ManyToManyField(
        PaymentMethod,
        through="Payment",
        verbose_name="métodos de pagamento",
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


class Payment(SoftDeletableModel, TimeStampedModel):
    cash_flow = models.ForeignKey(
        CashFlow,
        on_delete=models.CASCADE,
        verbose_name="fluxo de Caixa",
    )

    method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        verbose_name="método de pagamento",
    )

    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="valor",
    )

    def __str__(self):
        return f"{self.method.name} - R$ {self.amount}"

    class Meta:
        verbose_name = "pagamento"
        verbose_name_plural = "pagamentos"
