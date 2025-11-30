from django.contrib import admin
from .models import Editorial, Autor, Libro, PerfilAutor

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais', 'anio_fundacion']
    search_fields = ['nombre', 'pais']

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento']
    search_fields = ['nombre', 'apellido']
    list_filter = ['nacionalidad']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'isbn', 'editorial', 'fecha_publicacion']
    search_fields = ['titulo', 'isbn']
    list_filter = ['editorial', 'fecha_publicacion']
    filter_horizontal = ['autores']  # Widget para ManyToMany

@admin.register(PerfilAutor)
class PerfilAutorAdmin(admin.ModelAdmin):
    list_display = ['autor', 'email', 'sitio_web']
    search_fields = ['autor__nombre', 'autor__apellido']