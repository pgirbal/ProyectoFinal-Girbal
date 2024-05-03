from django.urls import path
from AppLab import views
from django.contrib.auth.views import LogoutView
from .views import PracticaListado, PracticaCreate, PracticaDelete, PracticaDetalle, PracticaUpdate

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('inicio/', views.inicio, name="Inicio"),
    path('docente', views.docente, name="Docente"),
    path('estudiante', views.estudiante, name="Estudiante"),
    path('buscar', views.buscar, name="Buscar"),

    #Path de prácticas
    path('practicaListado/', PracticaListado.as_view(), name = "practicas"),
    path('practicaDetalle/<int:pk>/', PracticaDetalle.as_view(), name = "practica"),
    path('practicaCreate', PracticaCreate.as_view(), name = "practica_crear"),
    path('practicaUpdate/<int:pk>/', PracticaUpdate.as_view(), name = "practica_editar"),
    path('practicaDelete/<int:pk>/', PracticaDelete.as_view(), name = "practica_borrar"),


    path('login', views.login, name="Login"),
    path('registro', views.registro, name='Registro'),
    path('logout', LogoutView.as_view(template_name='AppLab/logout.html'), name='Logout'),
]