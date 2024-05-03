from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class FormularioEstudiante(forms.Form):

    #Campos que tienen que llenar los estudiantes
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class FormularioDocente(forms.Form):

    #Campos que llena el docente a cargo
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    legajo = forms.IntegerField()

class FormularioPractica(forms.Form):
    
    #Campos a llenar para cargar una práctica a realizar
    nombre = forms.CharField(max_length=30)
    asignatura = forms.CharField(max_length=30)
    fecha = forms.DateField(label="Fecha (DD/MM/AAAA)")

class FormularioBuscar(forms.Form):
    asignatura = forms.CharField(max_length=30)

class FormularioRegistroUsuario(UserCreationForm):
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput)
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=20, label="Nombre de Usuario", widget=forms.TextInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}