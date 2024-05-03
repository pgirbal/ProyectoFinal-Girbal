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


def docente(request):

    if request.method == 'POST':

        miFormulario = FormularioDocente(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            docente = Docente (nombre=informacion["nombre"], 
                                  apellido=informacion["apellido"], 
                                  legajo=informacion["legajo"], 
                                  email=informacion["email"],
                                  )

            docente.save()

            return render(request, "AppLab/inicio.html")
        
    else:

        miFormulario= FormularioDocente() #Formulario vacío para construir el html

    return render(request, "AppLab/docente.html", {"FormularioDocente": miFormulario})

def estudiante(request):

    if request.method == 'POST':

        miFormulario = FormularioEstudiante(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante (nombre=informacion["nombre"], 
                                     apellido=informacion["apellido"], 
                                     email=informacion["email"],
                                     )

            estudiante.save()

            return render(request, "AppLab/inicio.html")
        
    else:

        miFormulario= FormularioEstudiante() #Formulario vacío para construir el html

    return render(request, "AppLab/estudiante.html", {"FormularioEstudiante": miFormulario})

def buscar(request):
    practicas = None

    if  "asignatura" in request.GET:
        asignatura = request.GET['asignatura'] 
        practicas = Practica.objects.filter(asignatura__icontains=asignatura)

    miFormulario = FormularioBuscar()
    
    return render(request, "AppLab/buscar.html", {"FormularioBuscar": miFormulario, "practicas": practicas})



#def listadoDocentes(request):
 #   docentes = Docente.objects.all()
  #  contexto = {"docentes":docentes}

  #  return render(request, "AppLab/listadoDocentes.html", contexto)

#def listadoEstudiantes(request):
 #   estudiantes = Estudiante.objects.all()
  #  contexto = {"estudiantes":estudiantes}

   # return render(request, "AppLab/listadoEstudiantes.html", contexto)

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

