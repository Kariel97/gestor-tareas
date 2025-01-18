# Gestor de Tareas API

Este es un proyecto de API RESTful para gestionar tareas, donde los usuarios pueden:
- Registrar nuevos usuarios
- Obtener un token JWT para autenticar solicitudes
- Crear, actualizar, eliminar y listar sus tareas
- Filtrar las tareas por estado (completadas o no)

### Características

- Registro de usuarios
- Autenticación con JWT (JSON Web Token)
- Gestión de tareas con las siguientes funcionalidades:
  - Listado de tareas
  - Creación de tareas
  - Actualización de tareas
  - Eliminación de tareas
  - Filtrado de tareas por estado
- Documentación interactiva de la API con Swagger

### Tecnologías utilizadas

- **Django**: Framework web para el desarrollo del backend.
- **Django REST Framework (DRF)**: Framework para crear APIs RESTful.
- **Django REST Framework SimpleJWT**: Para manejar la autenticación con JWT.
- **drf-yasg**: Para generar documentación interactiva con Swagger/OpenAPI.

### Requisitos

- Python 3.8 o superior
- Django 3.x o superior
- Django REST Framework
- Django REST Framework SimpleJWT
- drf-yasg (para Swagger)

### Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/Kariel97/gestor-tareas.git
   
2. **Crea un entorno virtual**:

   ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   
3. **Instala dependencias**:

   ```bash
   pip install -r requirements.txt
   
4. **Configura la base de datos**:

   ```bash
   python manage.py migrate
   
5. **Ejecuta el servidor**:

   ```bash
   python manage.py runserver
