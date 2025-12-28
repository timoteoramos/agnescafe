from django.contrib import admin
from .models import StockItem


@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("packet", "amount", "created",)
    list_filter = ("created", "modified",)
    search_fields = ("packet__name",)
