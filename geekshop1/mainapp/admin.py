from django.contrib import admin

# Register your models here.
from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
# admin.site.register(Product)

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', ('price', 'quantity'))  # прайс и количество в одну строку
    readonly_fields = ('description',)  # поле только для чтения, без возможности изменения
    ordering = ('name', 'price')  # сортировка
    search_fields = ('name',)
