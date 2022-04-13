from django.urls import path
from .views import home, signup, proveedores, delete_marca, products, increment_cantidad_prd, decrement_cantidad_prd,\
    delete_product, users, delete_user, clients, delete_client

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('proveedores/', proveedores, name='proveedores'),
    path('productos/', products, name='productos'),
    path('clients/', clients, name='clientes'),
    path('users/', users, name='users'),
    path('increment_prd/<id>/', increment_cantidad_prd, name='incrementar_prd'),
    path('decrement_prd/<id>/', decrement_cantidad_prd, name='decrementar_prd'),
    path('delete_proveedor/<id>/', delete_marca, name='delete_prov'),
    path('delete_product/<id>/', delete_product, name='delete_product'),
    path('delete_user/<id>/', delete_user, name='delete_user'),
    path('clients/delete_client/<id>/', delete_client, name='delete_client'),
]