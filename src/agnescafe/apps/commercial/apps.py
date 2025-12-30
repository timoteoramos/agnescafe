from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save

class CommercialConfig(AppConfig):
    name = "agnescafe.apps.commercial"
    verbose_name = "Comercial"

    def ready(self):
        from .signals import adjust_item, calculate_transaction
        from .models import Purchase, PurchaseItem, Sale, SaleItem

        pre_save.connect(adjust_item, sender=SaleItem)
        post_save.connect(calculate_transaction, sender=Purchase)
        post_save.connect(calculate_transaction, sender=PurchaseItem)
        post_save.connect(calculate_transaction, sender=Sale)
        post_save.connect(calculate_transaction, sender=SaleItem)
