from django.contrib import admin
from .models import Marca, Producto, Cliente
from .forms import AddProductForm, AddClientForm, AddMarcaForm


# Register your models here.


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10
    form = AddMarcaForm


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio_compra', 'precio_venta', 'cantidad', 'marca']
    list_per_page = 10
    list_filter = ['precio_compra', 'precio_venta', 'cantidad', 'marca']
    form = AddProductForm


class ClientAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'cedula', 'email', 'telefono', 'sexo']
    search_fields = ['nombres', 'apellidos', 'cedula', 'sexo']
    list_filter = ['telefono', 'sexo']
    form = AddClientForm


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClientAdmin)
