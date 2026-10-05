from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Producto


class RegistroConsumidorForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['email']
        if commit:
            usuario.save()
        return usuario


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'categoria', 'precio', 'stock')
        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'stock': 'Stock inicial',
        }


class CompraForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, initial=1, label='Cantidad')
