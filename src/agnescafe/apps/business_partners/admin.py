from django.contrib import admin
from .forms import ClientForm
from .models import Client, Supplier


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    form = ClientForm
    list_display = ("name", "house_number", "phone_number", "created",)
    search_fields = ("name", "house_number", "phone_number",)
    list_filter = ("created",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("name", "created",)
    search_fields = ("name",)
    list_filter = ("created",)
