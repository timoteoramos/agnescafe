from .models import Purchase, PurchaseItem, Sale, SaleItem
from agnescafe.apps.finnancial.models import CashFlow


def get_transaction_items(transaction, is_sale):
    if is_sale:
        return SaleItem.objects.filter(sale=transaction)
    else:
        return PurchaseItem.objects.filter(purchase=transaction)


def adjust_item(sender, **kwargs):
    if kwargs["instance"].price >= 0:
        kwargs["instance"].price = kwargs["instance"].product.price


def calculate_transaction(sender, **kwargs):
    is_sale = sender is Sale or sender is SaleItem
    total = 0

    transaction = kwargs["instance"] if (sender is Sale or sender is Purchase) else (kwargs["instance"].sale if is_sale else kwargs["instance"].purchase)

    for item in get_transaction_items(transaction, is_sale):
        total += item.amount * item.price

    if is_sale:
        total -= transaction.discount

    if not is_sale or transaction.paid:
        if not transaction.cash_flow:
            transaction.cash_flow = CashFlow(description=f"{"Venda" if is_sale else "Compra"} #{transaction.pk}")

        transaction.cash_flow.input = is_sale
        transaction.cash_flow.total = total
        transaction.cash_flow.save()

    (Sale if is_sale else Purchase).objects.filter(pk=transaction.pk).update(cash_flow=transaction.cash_flow, total=total)
