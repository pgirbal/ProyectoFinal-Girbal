from django.urls import path
from AppLab import views
from django.contrib.auth.views import LogoutView
from .views import PracticaListado, PracticaCreate, PracticaDelete, PracticaDetalle, PracticaUpdate
from .views import DocenteListado, DocenteCreate, DocenteDelete, DocenteDetalle, DocenteUpdate
from .views import EstudianteListado, EstudianteCreate, EstudianteDelete, EstudianteDetalle, EstudianteUpdate
from .views import Login, Registro, UsuarioEditar, PasswordCambio

urlpatterns = [

    path('', views.inicio, name = "inicio"),
    path('inicio', views.inicio, name = "inicio"),
    path('buscar/', views.buscar, name = "buscar"),

    #Path de prácticas
    path('practicaListado/', PracticaListado.as_view(), name = "practicas"),
    path('practicaDetalle/<int:pk>/', PracticaDetalle.as_view(), name = "practica"),
    path('practicaCreate', PracticaCreate.as_view(), name = "practica_crear"),
    path('practicaUpdate/<int:pk>/', PracticaUpdate.as_view(), name = "practica_editar"),
    path('practicaDelete/<int:pk>/', PracticaDelete.as_view(), name = "practica_borrar"),


    #Path de docentes
    path('docenteListado/', DocenteListado.as_view(), name = "docentes"),
    path('docenteDetalle/<int:pk>/', DocenteDetalle.as_view(), name = "docente"),
    path('docenteCreate', DocenteCreate.as_view(), name = "docente_crear"),
    path('docenteUpdate/<int:pk>/', DocenteUpdate.as_view(), name = "docente_editar"),
    path('docenteDelete/<int:pk>/', DocenteDelete.as_view(), name = "docente_borrar"),


    #Path de estudiantes
    path('estudianteListado/', EstudianteListado.as_view(), name = "estudiantes"),
    path('estudianteDetalle/<int:pk>/', EstudianteDetalle.as_view(), name = "estudiante"),
    path('estudianteCreate', EstudianteCreate.as_view(), name = "estudiante_crear"),
    path('estudianteUpdate/<int:pk>/', EstudianteUpdate.as_view(), name = "estudiante_editar"),
    path('estudianteDelete/<int:pk>/', EstudianteDelete.as_view(), name = "estudiante_borrar"),


    path('login/', Login.as_view(), name = "login"),
    path('registro/', Registro.as_view(), name = "registro"),
    path('logout/', LogoutView.as_view(template_name='AppLab/logout.html'), name = "logout"),
    path('edicionPerfil/', UsuarioEditar.as_view(), name = "editar_usuario"),
    path('passwordCambio/', PasswordCambio.as_view(), name = "editar_password"),
    path('passwordExitoso/', views.password_cambiado, name = "password_cambiado"),
]