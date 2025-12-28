from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel
from agnescafe.apps.catalog.models import Packet


class StockItem(SoftDeletableModel, TimeStampedModel):
    packet = models.ForeignKey(
        Packet,
        on_delete=models.CASCADE,
        verbose_name="pacote",
    )

    amount = models.PositiveIntegerField(
        verbose_name="quantidade",
    )

    def __str__(self):
        return f"{self.amount}x {self.packet}"

    class Meta:
        verbose_name = "item em estoque"
        verbose_name_plural = "itens em estoque"
