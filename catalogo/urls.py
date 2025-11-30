from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_libros, name='listar_libros'),
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('libro/nuevo/', views.crear_libro, name='crear_libro'),
    path('libro/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libro/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]