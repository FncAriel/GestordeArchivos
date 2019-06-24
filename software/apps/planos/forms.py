from django import forms
from apps.planos.models import proyecto, cliente, arquitecto, plano
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class proyectoForm(forms.ModelForm):
    class Meta:
        model = proyecto

        fields = [
            'inmobiliaria',
            'proyecto_inmobiliario',
            'entrega_total',
        ]

        labels = {
        'inmobiliaria':'Nombre Inmobiliaria',
        'proyecto_inmobiliario':'Nombre Proyecto',
        'entrega_total':'Fecha de entrega',
        }

        widgets = {
        'inmobiliaria': forms.TextInput(attrs={'class':'form-control'}),
        'proyecto_inmobiliario': forms.TextInput(attrs={'class':'form-control'}),
        'entrega_total': forms.TextInput(attrs={'class':'form-control'}),
        }

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }

class PlanoForm(forms.ModelForm):
    class Meta:
        model = plano
        fields = ('archivo', 'especificacion', 'arquitecto')

class ArquitectoForm(forms.ModelForm):
    class Meta:
        model = arquitecto
        fields = ('first_name', 'last_name', 'email', 'telefono', 'inmobiliaria')
