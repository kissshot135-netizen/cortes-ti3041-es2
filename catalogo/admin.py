from django.contrib import admin
from .models import Compra, Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre',)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'consumidor', 'cantidad', 'precio_unitario', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('nombre_producto', 'consumidor__username')
    readonly_fields = ('consumidor', 'producto', 'nombre_producto', 'precio_unitario', 'cantidad', 'fecha')