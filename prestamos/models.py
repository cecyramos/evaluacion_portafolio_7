from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Libro

class Prestamo(models.Model):
    """Gestión de préstamos de libros"""
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('DEVUELTO', 'Devuelto'),
        ('ATRASADO', 'Atrasado'),
    ]
    
    # Relación con el usuario que hace el préstamo
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )
    
    # Relación con el libro prestado
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )
    
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='ACTIVO'
    )
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Préstamos"
        ordering = ['-fecha_prestamo']
    
    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario.username}"