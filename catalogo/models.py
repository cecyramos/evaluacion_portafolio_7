from django.db import models

# REQUERIMIENTO 2: Entidad sin relaciones
class Editorial(models.Model):
    """Modelo simple sin relaciones con otras entidades"""
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Editoriales"
    
    def __str__(self):
        return self.nombre


# REQUERIMIENTO 3: Entidades con relaciones
class Autor(models.Model):
    """Autor de libros"""
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    """Libro con relaciones Uno a Muchos y Muchos a Muchos"""
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
    descripcion = models.TextField()
    
    # Relación Muchos a Muchos: Un libro puede tener varios autores
    # y un autor puede escribir varios libros
    autores = models.ManyToManyField(Autor, related_name='libros')
    
    # Relación Uno a Muchos: Una editorial puede publicar muchos libros
    # pero un libro pertenece a una sola editorial
    editorial = models.ForeignKey(
        Editorial, 
        on_delete=models.CASCADE,
        related_name='libros'
    )
    
    class Meta:
        verbose_name_plural = "Libros"
    
    def __str__(self):
        return self.titulo


class PerfilAutor(models.Model):
    """Relación Uno a Uno con Autor"""
    # Relación Uno a Uno: Cada autor tiene un único perfil
    autor = models.OneToOneField(
        Autor,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    sitio_web = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    premios = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Perfiles de Autores"
    
    def __str__(self):
        return f"Perfil de {self.autor}"