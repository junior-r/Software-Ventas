from django.urls import path
from .views import home, signup, proveedores, delete_proveedor, products, increment_cantidad_prd, \
    decrement_cantidad_prd, delete_product, users, delete_user, clients, delete_client, edit_product, \
    edit_proveedor, view_product, edit_client, ventas, add_prd_cart, sub_prd_cart, delete_prd_cart, \
    clean_cart, factura_ventas

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('proveedores/', proveedores, name='proveedores'),
    path('productos/', products, name='productos'),
    path('clients/', clients, name='clientes'),
    path('ventas/', ventas, name='ventas'),
    path('users/', users, name='users'),
    # Acciones del Carrito
    path('add_cart/<int:id>/', add_prd_cart, name='add_cart'),
    path('sub_cart/<int:id>/', sub_prd_cart, name='sub_cart'),
    path('delete_prd_cart/<int:id>/', delete_prd_cart, name='del_prd_cart'),
    path('clean_cart/', clean_cart, name='clean_cart'),
    #Acciones de los Productos
    path('increment_prd/<id>/', increment_cantidad_prd, name='incrementar_prd'),
    path('decrement_prd/<id>/', decrement_cantidad_prd, name='decrementar_prd'),
    path('view_product/<id>/', view_product, name='view_producto'),
    path('edit_producto/<id>/', edit_product, name='edit_producto'),
    path('delete_product/<id>/', delete_product, name='delete_product'),
    # Acciones de Clientes
    path('edit_cliente/<id>/', edit_client, name='edit_client'),
    path('clients/delete_client/<id>/', delete_client, name='delete_client'),
    # Acciones de Proveedores
    path('edit_proveedor/<id>/', edit_proveedor, name='edit_proveedor'),
    path('delete_proveedor/<id>/', delete_proveedor, name='delete_prov'),
    # Acciones de Usuarios
    path('delete_user/<id>/', delete_user, name='delete_user'),
    # Factura de ventas
    path('factura/<int:id>/', factura_ventas, name='factura_ventas'),
]