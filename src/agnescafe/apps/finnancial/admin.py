from django.contrib import admin
from .models import CashFlow, Payment, PaymentMethod


class PaymentInline(admin.StackedInline):
    exclude = ["is_removed"]
    model = Payment
    extra = 1


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    inlines = [PaymentInline]
    list_display = ("description", "input", "total", "created",)
    list_filter = ("input", "created",)
    search_fields = ("description",)
    ordering = ("-created",)


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("name", "created",)
    search_fields = ("name",)
    ordering = ("name",)
