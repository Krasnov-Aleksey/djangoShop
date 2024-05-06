from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity_product=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'added_date_product']
    ordering = ['name_product']
    list_filter = ['price_product']
    search_fields = ['added_date_product']
    search_help_text = 'Поиск по дате'
    actions = [reset_quantity]
    fields = ['name_product', 'description_product','quantity_product', 'added_date_product']
    readonly_fields = ['added_date_product']


admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
