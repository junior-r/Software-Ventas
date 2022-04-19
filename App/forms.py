from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App.models import Marca, Producto, Cliente


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class AddProductForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Por seguridad ingrese su nombre de usuario, ej: john'}))

    def clean_username(self):  # Valida si el usuario existe en la Base de Datos
        username = self.cleaned_data['username']
        exists = User.objects.filter(username=username).exists()
        if exists:
            return username
        else:
            raise ValidationError('Usuario Inválido')

    class Meta:
        model = Producto
        fields = '__all__'


options_sex = (
    ('--', '-----'),
    ('F', 'Femenino'),
    ('M', 'Masculino')
)


class AddClientForm(forms.ModelForm):
    nombres = forms.CharField(max_length=150, required=True)
    apellidos = forms.CharField(max_length=150, required=True)
    cedula = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField(required=True)
    sexo = forms.ChoiceField(required=True, choices=options_sex)

    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'cedula', 'email', 'telefono', 'sexo']
        exclude = ['productos_comprados']


class AddMarcaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=150, required=True)
    telefono = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Marca
        fields = '__all__'
