from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save

class CommercialConfig(AppConfig):
    name = "agnescafe.apps.commercial"
    verbose_name = "Comercial"

    def ready(self):
        from .signals import calculate_sale, adjust_item
        from .models import Sale, SaleItem

        pre_save.connect(adjust_item, sender=SaleItem)
        post_save.connect(calculate_sale, sender=Sale)
        post_save.connect(calculate_sale, sender=SaleItem)
