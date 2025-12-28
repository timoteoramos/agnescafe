from django.contrib import admin
from .models import CashFlow


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("description", "input", "total", "created",)
    list_filter = ("input", "created",)
    search_fields = ("description",)
    ordering = ("-created",)
