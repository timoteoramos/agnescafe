from django.contrib import admin
from .models import Purchase, PurchaseItem, Sale, SaleItem


class PurchaseItemInline(admin.StackedInline):
    exclude = ["is_removed"]
    model = PurchaseItem
    extra = 1


class SaleItemInline(admin.StackedInline):
    exclude = ["is_removed"]
    model = SaleItem
    extra = 1


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("supplier", "total", "created",)
    list_filter = ("created",)
    readonly_fields = ("cash_flow", "total",)
    search_fields = ("supplier__name",)
    inlines = [PurchaseItemInline]
    ordering = ("-created",)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("client", "total", "paid", "created",)
    list_filter = ("paid", "created",)
    readonly_fields = ("cash_flow", "total",)
    search_fields = ("client__name",)
    inlines = [SaleItemInline]
    ordering = ("-created",)
