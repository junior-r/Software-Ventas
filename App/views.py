from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, AddProductForm, AddClientForm, AddMarcaForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Marca, Producto, Cliente
import datetime

# Create your views here.

date = datetime.datetime.now()


def home(request):
    data = {
        'date': date
    }
    return render(request, 'app/home.html', data)


def signup(request):
    data = {
        'form': SignUpForm
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Cuenta creada correctamente!')
            return redirect(to='home')
        else:
            data['form'] = form

    return render(request, 'registration/signup.html', data)


@login_required
def products(request):
    user = User.objects.get(username=request.user)
    productos = Producto.objects.filter(username=user.username)
    search = request.GET.get('search')  # Este es el valor del input name='search' en el template

    username = ''
    ganancias = 0
    cantidad = 0
    ganancia_total = 0
    for i in productos:
        username = i.get_username()
        ganancias += i.get_utilities_prd()
        cantidad += i.cantidad
        ganancia_total += i.get_utilities_total()
        # Esta es un suma secuencial de todas las ganancias por producto para dar una ganancia general

    data = {
        'productos': productos,
        'form': AddProductForm(),
        'username': username,
        'ganancias': ganancias,
        'totalproductos': cantidad,
        'ganancia_total': ganancia_total,
        'date': date
    }

    if search:
        try:
            result_prd = Producto.objects.filter(
                Q(id__icontains=search) |
                Q(nombre__icontains=search) |
                Q(marca__nombre__icontains=search) |
                Q(username__icontains=search)
            ).distinct()
            data['result_prd'] = result_prd
        except ValueError as ve:
            messages.error(request, 'Solo se puede buscar por Id, Nombre, Marca y Usuario')

    if request.method == 'POST':
        current_user = request.POST['username']
        try:
            user = User.objects.get(username=current_user)
            form = AddProductForm(request.POST)
            if form.is_valid() and current_user == user.username:
                form.save()
                messages.success(request, 'Producto agregado correctamente!')
                return redirect(to='productos')
            else:
                messages.error(request, 'Algún dato es inválido')
                data['form'] = form
        except:
            messages.error(request, 'Usuario es inválido')
            return redirect(to='productos')

    return render(request, 'app/productos.html', data)


@login_required
def increment_cantidad_prd(request, id):
    # Incrementa la cantidad del producto de 1 en 1
    producto = Producto.objects.filter(id=id)
    for p in producto:
        cantidad = p.cantidad
        producto.update(cantidad=cantidad + 1)

    return redirect(to='productos')


@login_required
def decrement_cantidad_prd(request, id):
    # Reduce la cantidad del producto de 1 en 1
    producto = Producto.objects.filter(id=id)
    for p in producto:
        cantidad = p.cantidad
        producto.update(cantidad=cantidad - 1)

    return redirect(to='productos')


@login_required
def delete_product(request, id):
    """
        Buscamos el producto en la Base de Datos, y se borra.
        Hay una alerta JavaScript de confirmación en el template.
    """
    product = get_object_or_404(Producto, id=id)
    product.delete()
    messages.success(request, 'Producto borrado exitosamente!')
    return redirect(to='productos')


@login_required
def proveedores(request):
    marcas = Marca.objects.all()

    data = {
        'proveedores': marcas,
        'form': AddMarcaForm(),
        'date': date
    }

    if request.method == 'POST':
        form = AddMarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor registrado con éxito!')
            return redirect(to='proveedores')
        else:
            messages.error(request, 'Algún dato es inválido. Intente otra vez.')
            data['form_proveedor'] = form

    return render(request, 'app/marcas.html', data)


@login_required
def delete_marca(request, id):
    prov = get_object_or_404(Marca, id=id)
    prov.delete()
    messages.success(request, 'Proveedor eliminado existosamente!')
    return redirect(to='proveedores')


@login_required
def users(request):
    all_users = User.objects.all()

    data = {
        'all_users': all_users,
        'form': SignUpForm,
        'date': date
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente!')
            return redirect(to='users')
        else:
            data['form'] = form

    return render(request, 'app/users.html', data)


@login_required
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, 'Usuario eliminado correctamente!')
    return redirect(to='users')


@login_required
def clients(request):
    clients = Cliente.objects.all()
    busqueda = request.GET.get('search')

    data = {
        'form': AddClientForm,
        'clientes': clients,
        'date': date
    }

    if busqueda:
        result_client = Cliente.objects.filter(
            Q(id__icontains=busqueda) |
            Q(nombres__icontains=busqueda) |
            Q(cedula__icontains=busqueda)
        ).distinct()
        data['result_search'] = result_client

    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado con éxito!')
            return redirect(to='clientes')
        else:
            messages.error(request, 'Hubo algún error, intente de nuevo!')
            data['form'] = form

    return render(request, 'app/clientes.html', data)


@login_required
def delete_client(request, id):
    client = get_object_or_404(Cliente, id=id)
    client.delete()
    messages.success(request, 'Cliente eliminado exitosamente!')
    return redirect(to='clientes')
