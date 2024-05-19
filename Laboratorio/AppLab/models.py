from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Practica(models.Model):

    nombre = models.CharField(max_length=40)
    asignatura = models.CharField(max_length=30)
    fecha = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Asignatura: {self.asignatura} - Fecha: {self.fecha}"

class Docente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Legajo: {self.legajo} - e-mail: {self.email}"

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - e-mail: {self.email}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username
