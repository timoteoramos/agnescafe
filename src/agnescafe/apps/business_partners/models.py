from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class Client(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(
        max_length=64,
        verbose_name="nome",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

class Supplier(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(
        max_length=64,
        verbose_name="nome",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "fornecedor"
        verbose_name_plural = "fornecedores"
