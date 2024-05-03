from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from AppLab.models import Estudiante, Practica, Docente
from AppLab.forms import FormularioEstudiante, FormularioDocente, FormularioPractica, FormularioBuscar, FormularioRegistroUsuario

# Create your views here.

def inicio(request):

    return render(request, "AppLab/inicio.html")

#Definición de prácticas como CBV

class PracticaListado(ListView):
    model = Practica
    context_object_name = "practicas"
    template_name = "AppLab/practicaListado.html"

class PracticaDetalle(DetailView):
    model = Practica
    context_object_name = "practica"
    template_name = "AppLab/practicaDetalle.html"

class PracticaCreate(LoginRequiredMixin, CreateView):
    model = Practica
    template_name = "AppLab/practicaCrear.html"
    success_url = reverse_lazy('practicas')
    fields = ['nombre', 'asignatura', 'fecha']
    login_url = '/login'

class PracticaUpdate(LoginRequiredMixin, UpdateView):
    model = Practica
    template_name = "AppLab/practicaEditar.html"
    success_url = reverse_lazy('practicas')
    fields = ['nombre', 'asignatura', 'fecha']
    login_url = '/login'

class PracticaDelete(LoginRequiredMixin, DeleteView):
    model = Practica
    template_name = "AppLab/practicaBorrar.html"
    success_url = reverse_lazy('practicas')
    login_url = '/login'



#Definición de docentes como CBV

class DocenteListado(ListView):
    model = Docente
    context_object_name = "docentes"
    template_name = "AppLab/docenteListado.html"

class DocenteDetalle(DetailView):
    model = Docente
    context_object_name = "docente"
    template_name = "AppLab/docenteDetalle.html"

class DocenteCreate(LoginRequiredMixin, CreateView):
    model = Docente
    template_name = "AppLab/docenteCrear.html"
    success_url = reverse_lazy('docentes')
    fields = ['nombre', 'apellido', 'legajo', 'email']
    login_url = '/login'

class DocenteUpdate(LoginRequiredMixin, UpdateView):
    model = Docente
    template_name = "AppLab/docenteEditar.html"
    success_url = reverse_lazy('docentes')
    fields = ['nombre', 'apellido', 'legajo', 'email']
    login_url = '/login'

class DocenteDelete(LoginRequiredMixin, DeleteView):
    model = Docente
    template_name = "AppLab/docenteBorrar.html"
    success_url = reverse_lazy('docentes')
    login_url = '/login'


#Definición de estudiantes como CBV

class EstudianteListado(ListView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "AppLab/estudianteListado.html"

class EstudianteDetalle(DetailView):
    model = Estudiante
    context_object_name = "estudiante"
    template_name = "AppLab/estudianteDetalle.html"

class EstudianteCreate(LoginRequiredMixin, CreateView):
    model = Estudiante
    template_name = "AppLab/estudianteCrear.html"
    success_url = reverse_lazy('estudiantes')
    fields = ['nombre', 'apellido', 'email']
    login_url = '/login'

class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    template_name = "AppLab/estudianteEditar.html"
    success_url = reverse_lazy('estudiantes')
    fields = ['nombre', 'apellido', 'email']
    login_url = '/login'

class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name = "AppLab/estudianteBorrar.html"
    success_url = reverse_lazy('estudiantes')
    login_url = '/login'


def buscar(request):
    practicas = None

    if  "asignatura" in request.GET:
        asignatura = request.GET['asignatura'] 
        practicas = Practica.objects.filter(asignatura__icontains=asignatura)

    miFormulario = FormularioBuscar()
    
    return render(request, "AppLab/buscar.html", {"FormularioBuscar": miFormulario, "practicas": practicas})


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "AppLab/inicio.html", {"mensaje":f"¡Hola {usuario}!"})

            else:

                return render(request, "AppLab/inicio.html", {"mensaje":"Datos incorrectos, por favor intente nuevamente."})

        else:
            return render(request, "AppLab/inicio.html", {"mensaje":"Formulario erróneo."})

    form = AuthenticationForm()

    return render(request, "AppLab/login.html", {"form": form})

def registro(request):

    if request.method == "POST":
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid:

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppLab/inicio.html", {"mensaje":"Usuario creado correctamente"})

    else:
        form = FormularioRegistroUsuario()

    return render(request, "AppLab/registro.html", {'form': form})

