"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('editmedidor/<int:id>', views.editarMedidor, name='editarMedidor'),
        path('deletemedidor/<int:id>', views.eliminarMedidor, name='eliminarMedidor'),
        path('logout/', views.logout_view, name="logout_view"),
        path('login/', views.ingreso, name="login"),
]