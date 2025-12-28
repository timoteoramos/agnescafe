from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class MeasurementModel(models.Model):
    class Measurement(models.TextChoices):
        UNIT = "UN", "unidade"
        GRAM = "G", "grama"
        LITER = "L", "litro"

    measurement = models.CharField(
        max_length=2,
        choices=Measurement.choices,
        default = Measurement.UNIT,
        verbose_name="unidade de medida",
    )

    class Meta:
        abstract = True


class Input(MeasurementModel, SoftDeletableModel, TimeStampedModel):
    name = models.CharField(
        max_length=64,
        verbose_name="nome",
    )

    amount = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name="quantidade",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "insumo"
        verbose_name_plural = "insumos"


class Packet(SoftDeletableModel, TimeStampedModel):
    input = models.ForeignKey(
        Input,
        on_delete=models.CASCADE,
        verbose_name="insumo",
    )

    name = models.CharField(
        max_length=64,
        verbose_name="nome",
    )

    amount = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name="quantidade",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "pacote"
        verbose_name_plural = "pacotes"


class Product(MeasurementModel, SoftDeletableModel, TimeStampedModel):
    name = models.CharField(
        max_length=64,
        verbose_name="nome",
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="preço",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"


class ProductInput(SoftDeletableModel, TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="inputs",
        verbose_name="produto",
    )

    input = models.ForeignKey(
        Input,
        on_delete=models.CASCADE,
        verbose_name="insumo",
    )

    amount = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name="quantidade",
    )

    def __str__(self):
        return f"{self.amount} {self.input.measurement} {self.input.name}"

    class Meta:
        unique_together = ("product", "input",)
        verbose_name = "insumo do produto"
        verbose_name_plural = "insumos do produto"
