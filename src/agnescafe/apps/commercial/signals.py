from .models import Sale, SaleItem
from agnescafe.apps.finnancial.models import CashFlow


def adjust_item(sender, **kwargs):
    if kwargs["instance"].price >= 0:
        kwargs["instance"].price = kwargs["instance"].product.price


def calculate_sale(sender, **kwargs):
    total = 0
    sale = kwargs["instance"] if sender is Sale else kwargs["instance"].sale

    for item in SaleItem.objects.filter(sale=sale):
        total += item.amount * item.price

    total -= sale.discount

    if sale.paid:
        if not sale.cash_flow:
            sale.cash_flow = CashFlow(description=f"Venda #{sale.pk}")

        sale.cash_flow.input = True
        sale.cash_flow.total = total
        sale.cash_flow.save()

    Sale.objects.filter(pk=sale.pk).update(cash_flow=sale.cash_flow, total=total)
