from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Libro, Autor, Editorial

# CREATE - Crear libro
def crear_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        isbn = request.POST.get('isbn')
        fecha_publicacion = request.POST.get('fecha_publicacion')
        numero_paginas = request.POST.get('numero_paginas')
        descripcion = request.POST.get('descripcion')
        editorial_id = request.POST.get('editorial')
        
        libro = Libro.objects.create(
            titulo=titulo,
            isbn=isbn,
            fecha_publicacion=fecha_publicacion,
            numero_paginas=numero_paginas,
            descripcion=descripcion,
            editorial_id=editorial_id
        )
        
        # Agregar autores (ManyToMany)
        autores_ids = request.POST.getlist('autores')
        libro.autores.set(autores_ids)
        
        messages.success(request, 'Libro creado exitosamente')
        return redirect('listar_libros')
    
    # GET - Mostrar formulario
    editoriales = Editorial.objects.all()
    autores = Autor.objects.all()
    return render(request, 'crear_libro.html', {
        'editoriales': editoriales,
        'autores': autores
    })

# READ - Listar libros
def listar_libros(request):
    libros = Libro.objects.all().select_related('editorial').prefetch_related('autores')
    return render(request, 'listar_libros.html', {'libros': libros})

# READ - Detalle de libro
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'detalle_libro.html', {'libro': libro})

# UPDATE - Editar libro
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    
    if request.method == 'POST':
        libro.titulo = request.POST.get('titulo')
        libro.isbn = request.POST.get('isbn')
        libro.fecha_publicacion = request.POST.get('fecha_publicacion')
        libro.numero_paginas = request.POST.get('numero_paginas')
        libro.descripcion = request.POST.get('descripcion')
        libro.editorial_id = request.POST.get('editorial')
        libro.save()
        
        # Actualizar autores
        autores_ids = request.POST.getlist('autores')
        libro.autores.set(autores_ids)
        
        messages.success(request, 'Libro actualizado exitosamente')
        return redirect('detalle_libro', libro_id=libro.id)
    
    editoriales = Editorial.objects.all()
    autores = Autor.objects.all()
    return render(request, 'editar_libro.html', {
        'libro': libro,
        'editoriales': editoriales,
        'autores': autores
    })

# DELETE - Eliminar libro
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente')
        return redirect('listar_libros')
    
    return render(request, 'eliminar_libro.html', {'libro': libro})