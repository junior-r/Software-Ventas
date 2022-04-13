from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField()
    marca = models.ForeignKey(Marca,  null=True, blank=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=100)

    def get_username(self):
        return self.username

    def get_utilities_prd(self):
        return self.precio_venta - self.precio_compra

    def get_utilities_total(self):
        return (self.precio_venta - self.precio_compra) * self.cantidad

    def __str__(self):
        return '{}'.format(self.nombre)


options_sex = (
    ('F', 'Femenino'),
    ('M', 'Masculino')
)


class Cliente(models.Model):
    nombres = models.CharField(max_length=150, unique=False, blank=False)
    apellidos = models.CharField(max_length=150, unique=False, blank=False)
    cedula = models.IntegerField(unique=True, blank=False)
    email = models.EmailField(unique=False, blank=False)
    telefono = models.IntegerField(unique=False, blank=False)
    sexo = models.CharField(choices=options_sex, unique=False, blank=False, max_length=9)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
