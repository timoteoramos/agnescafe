from django.contrib import admin
from .models import Client, Supplier


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("name", "created",)
    search_fields = ("name",)
    list_filter = ("created",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("name", "created",)
    search_fields = ("name",)
    list_filter = ("created",)
