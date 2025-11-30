from django.contrib import admin
from .models import Prestamo

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['libro', 'usuario', 'fecha_prestamo', 'fecha_devolucion_esperada', 'estado']
    list_filter = ['estado', 'fecha_prestamo']
    search_fields = ['libro__titulo', 'usuario__username']
    date_hierarchy = 'fecha_prestamo'