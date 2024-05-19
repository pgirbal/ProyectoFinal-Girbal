from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from AppLab.models import Estudiante, Practica, Docente
from AppLab.forms import FormularioBuscar, FormularioRegistroUsuario, FormularioCambioPassword, FormularioEdicionUsuario

# Create your views here.

def inicio(request):

    return render(request, "AppLab/inicio.html")


#Interacciones de usuario con su cuenta

class Login(LoginView):
    template_name = "AppLab/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')
    

class Registro(FormView):
    template_name = "AppLab/registro.html"
    form_class = FormularioRegistroUsuario
    redirect_authenticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registro, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(Registro, self).get(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    

class UsuarioEditar(UpdateView):
    form_class = FormularioEdicionUsuario
    template_name = "AppLab/usuarioEditar.html"
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user
    

class PasswordCambio(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = "AppLab/passwordCambio.html"
    success_url = reverse_lazy('password_cambiado')


def password_cambiado(request):
    return render(request, "AppLab/passwordExitoso.html", {})


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


def about(request):
    return render(request, 'AppLab/acercaDeMi.html', {})
