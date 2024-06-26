from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

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
    email = forms.EmailField()
    username = forms.CharField(max_length=20, label="Nombre de Usuario", widget=forms.TextInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)
 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'avatar']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            avatar = self.cleaned_data.get('avatar')
            if avatar:
                UserProfile.objects.create(user=user, avatar=avatar)
            else:
                UserProfile.objects.create(user=user)
        return user


class FormularioEdicionUsuario(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput)
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput)
    username = forms.CharField(max_length=20, label="Nombre de Usuario", widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')


class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña actual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Repita nueva contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')