from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel
from agnescafe.apps.business_partners.models import Client, Supplier
from agnescafe.apps.catalog.models import Packet, Product
from agnescafe.apps.finnancial.models import CashFlow


class BaseOperation(SoftDeletableModel, TimeStampedModel):
    cash_flow = models.ForeignKey(
        CashFlow,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="fluxo de Caixa",
    )

    total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name="total",
    )

    def __str__(self):
        return f"{self.created} - R$ {self.total}"

    class Meta:
        abstract = True


class Purchase(BaseOperation):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name="fornecedor",
    )

    packets = models.ManyToManyField(
        Packet,
        through="PurchaseItem",
        verbose_name="pacotes",
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "compra"
        verbose_name_plural = "compras"


class PurchaseItem(SoftDeletableModel, TimeStampedModel):
    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="compra",
    )

    packet = models.ForeignKey(
        Packet,
        on_delete=models.CASCADE,
        verbose_name="pacote",
    )

    amount = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name="quantidade",
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="preço",
    )

    def __str__(self):
        return f"{self.amount}x {self.packet.name}"

    class Meta:
        unique_together = ("purchase", "packet",)
        verbose_name = "item da compra"
        verbose_name_plural = "itens da compra"


class Sale(BaseOperation):
    client = models.ForeignKey(
        Client,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="cliente",
    )

    products = models.ManyToManyField(
        Product,
        through="SaleItem",
        verbose_name="produtos",
    )

    discount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        verbose_name="desconto",
    )

    paid = models.BooleanField(
        default=False,
        verbose_name="pago",
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "venda"
        verbose_name_plural = "vendas"


class SaleItem(SoftDeletableModel, TimeStampedModel):
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="venda",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="produto",
    )

    amount = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name="quantidade",
    )

    price = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        verbose_name="preço",
    )

    def __str__(self):
        return f"{self.amount} {self.product.measurement} {self.product.name}"

    class Meta:
        unique_together = ("sale", "product",)
        verbose_name = "item da venda"
        verbose_name_plural = "itens da venda"
