from django.contrib import admin
from .models import Categoria, ProductoGym


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('nombre',)


@admin.register(ProductoGym)
class ProductoGymAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'categoria',
        'marca',
        'precio_clp',
        'stock',
        'disponible',
        'fecha_ingreso',
    )
    list_filter = ('categoria', 'disponible', 'fecha_ingreso')
    search_fields = ('nombre', 'marca', 'categoria__nombre')