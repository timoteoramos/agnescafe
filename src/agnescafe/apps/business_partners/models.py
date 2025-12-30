from django.db import models
from django.urls import reverse
from model_utils.models import SoftDeletableModel, TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class Client(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(
        max_length=64,
        verbose_name="nome",
    )

    house_number = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name="número da casa",
    )

    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name="número de telefone",
    )

    def __str__(self):
        return f"{self.name} - {self.house_number}" if self.house_number else self.name

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})

    def get_pending_orders(self):
        return self.sale_set.filter(paid=False)

    def has_pending_orders(self):
        return self.get_pending_orders().count() > 0

    def total_pending_amount(self):
        return sum(order.total for order in self.get_pending_orders())

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
