from django.contrib import admin
from .models import Input, Packet, Product, ProductInput


class ProductInputInline(admin.StackedInline):
    exclude = ["is_removed"]
    model = ProductInput
    extra = 1


@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("name", "amount", "created",)
    search_fields = ("name",)
    list_filter = ("created",)


@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    list_display = ("name", "amount", "created",)
    search_fields = ("name",)
    list_filter = ("created",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ["is_removed"]
    inlines = [ProductInputInline]
    list_display = ("name", "price", "created",)
    search_fields = ("name",)
    list_filter = ("created",)
