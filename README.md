# Sistema de Gestión de Biblioteca - Django

Proyecto desarrollado para el bootcamp de Python + Django, implementando todas las funcionalidades de integración con bases de datos.

## Requerimientos Cumplidos
### 1. Integración con Base de Datos ✓

- Configuración de Django con SQLite
- Gestión de conexiones mediante ORM
- Configuración en settings.py con DATABASES y TEMPLATES

### 2. Modelos sin Relaciones ✓

- Modelo Editorial implementado como entidad independiente

### 3. Modelos con Relaciones ✓

- Uno a Uno: Autor ↔ PerfilAutor (OneToOneField)
- Uno a Muchos: Editorial → Libro (ForeignKey)
- Muchos a Muchos: Libro ↔ Autor (ManyToManyField)

### 4. Migraciones ✓

- Migraciones creadas y aplicadas para todos los modelos
- Comandos: makemigrations y migrate

### 5. Consultas ORM y SQL ✓

- Filtros con filter(), exclude(), get()
- Agregaciones con annotate() y aggregate()
- Consultas SQL personalizadas con raw() y cursor()
- Todas las consultas ejecutadas en Django shell (ver consultas.txt)

### 6. Aplicación CRUD ✓

- Create: Crear libros con formulario
- Read: Listar y ver detalles de libros
- Update: Editar libros existentes
- Delete: Eliminar libros con confirmación

### 7. Aplicaciones Preinstaladas ✓

- Panel de administración (django.contrib.admin)
- Sistema de autenticación (django.contrib.auth)
- Gestión de sesiones (django.contrib.sessions)
- Sistema de mensajes (django.contrib.messages)

## Estructura del Proyecto
```
evaluacion_portafolio_7/
├── .gitignore
├── README.md
├── requirements.txt
├── consultas.txt             # Consultas ORM/SQL para el shell
├── datos_ejemplo.txt         # Datos para poblar la BD
├── manage.py
├── db.sqlite3               # Base de datos SQLite
├── capturas/                # Carpeta para screenshots
│   └── (capturas de pantalla)
├── biblioteca_project/
│   ├── settings.py          # Configuración (DATABASES, TEMPLATES)
│   └── urls.py
├── catalogo/
│   ├── admin.py             # Configuración del admin
│   ├── models.py            # Modelos con relaciones
│   ├── views.py             # Vistas CRUD
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│       ├── base.html
│       ├── listar_libros.html
│       ├── crear_libro.html
│       ├── detalle_libro.html
│       ├── editar_libro.html
│       └── eliminar_libro.html
└── prestamos/
    ├── admin.py
    ├── models.py
    └── migrations/
```
---

## Instalación y Configuración
### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
### 1. Clonar el repositorio
```bash
git clone https://github.com/cecyramos/evaluacion_portafolio_7.git
```
### 2. Crear entorno virtual
```bash
python -m venv myenv

# Activar en Windows:
myenv\Scripts\activate

# Activar en Linux/Mac:
source myenv/bin/activate
```
### 3. Instalar Django
```bash
pip install django
```
### 4. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Crear superusuario para el admin
```bash
python manage.py createsuperuser

# Ingresar: usuario, email y contraseña
```

### 6. Poblar base de datos
Abrir el admin en http://127.0.0.1:8000/admin/ y agregar:

- Editoriales
- Autores
- Libros

O copiar los datos desde datos_ejemplo.txt manualmente en el admin.

### 7. Ejecutar consultas del Requerimiento 5
```bash
python manage.py shell

# Luego copiar y pegar las consultas desde comandos.txt
```

### 8. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```
Acceder a:
- Aplicación web: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

## Funcionalidades Principales

### CRUD de Libros (Interfaz Web)
- Listar: / - Ver todos los libros
- Crear: /libro/nuevo/ - Agregar nuevo libro
- Detalle: /libro/<id>/ - Ver detalles de un libro
- Editar: /libro/<id>/editar/ - Modificar libro
- Eliminar: /libro/<id>/eliminar/ - Borrar libro

### Panel de Administración
- Gestión completa de Editoriales, Autores, Libros, Perfiles y Préstamos
- Filtros de búsqueda avanzados
- Widgets especiales para relaciones ManyToMany
- Ordenamiento y paginación

### Consultas ORM/SQL (Shell)

Todas las consultas del Requerimiento 5 están en comandos.txt:

- Filtrado con filter() y exclude()
- Consultas complejas con Q objects
- Agregaciones con annotate() y aggregate()
- Consultas SQL raw
- Navegación por relaciones

## Modelos de Datos

### Editorial (Sin relaciones - Req. 2)
```
- nombre: CharField
- pais: CharField
- anio_fundacion: IntegerField
```
### Autor
```
- nombre: CharField
- apellido: CharField
- fecha_nacimiento: DateField
- nacionalidad: CharField
- biografia: TextField
```

### PerfilAutor (Relación 1:1 con Autor - Req. 3)
```
- autor: OneToOneField(Autor)
- sitio_web: URLField
- email: EmailField
- premios: TextField
```

### Libro (Relaciones 1:N y N:M - Req. 3)
```
- titulo: CharField
- isbn: CharField (unique)
- fecha_publicacion: DateField
- numero_paginas: IntegerField
- descripcion: TextField
- autores: ManyToManyField(Autor)      # Relación N:M
- editorial: ForeignKey(Editorial)      # Relación 1:N
```

### Prestamo
```
- usuario: ForeignKey(User)
- libro: ForeignKey(Libro)
- fecha_prestamo: DateField
- fecha_devolucion_esperada: DateField
- fecha_devolucion_real: DateField
- estado: CharField (choices)
- notas: TextField
```

## Ejemplos de Consultas (consultas.txt)
```
# Filtro básico
Libro.objects.filter(editorial__nombre="Planeta")

# Filtro con OR
Libro.objects.filter(Q(titulo__icontains="amor") | Q(titulo__icontains="cien"))

# Agregación
Editorial.objects.annotate(total_libros=Count('libros'))

# SQL Raw
Libro.objects.raw('SELECT * FROM catalogo_libro WHERE numero_paginas > 300')

# Cursor SQL directo
with connection.cursor() as cursor:
    cursor.execute('SELECT ...')
    resultados = cursor.fetchall()
```

## Tecnologías Utilizadas
- Backend: Python 3.x, Django 4.x
- Base de datos: SQLite3
- Frontend: HTML5, Bootstrap 5
- ORM: Django ORM

## Notas Importantes
- Consultas avanzadas: Se ejecutan directamente en el shell de Django, no en vistas web
- Capturas: La carpeta capturas/ contiene screenshots del proyecto en funcionamiento

## Archivos Clave

- settings.py: Configuración de BD y templates
- models.py: Definición de modelos con relaciones
- views.py: Lógica CRUD
- admin.py: Configuración del panel admin
- consultas.txt: Todas las consultas ORM/SQL del Requerimiento 5
- datos_ejemplo.txt: Datos de ejemplo para la BD

---

## Autor

Cecilia Ramos - 2025

---

## Licencia

Este proyecto es de código abierto bajo la licencia MIT.
