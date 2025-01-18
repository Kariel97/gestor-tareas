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
   cd gestor-tareas
   
   
2. **Crea un entorno virtual**:

   ```bash
    python -m venv venv
    source venv/Scripts/activate  # En Windows usa `venv\Scripts\activate`
   
3. **Instala dependencias**:

   ```bash
   pip install -r requirements.txt
   
4. **Configura la base de datos**:

   ```bash
   python manage.py migrate
   
5. **Ejecuta el servidor**:

   ```bash
   python manage.py runserver
   
   
5. **Ver API**:

   ```bash
   http://127.0.0.1:8000/api/register/
   
# Documentación Swagger
Para acceder a la documentación interactiva de la API con Swagger, visita: http://127.0.0.1:8000/swagger/


# Ejemplo de Peticiones cURL

  **Crear un usuario**:
  
    curl -X POST http://127.0.0.1:8000/api/register/ \
      -H "Content-Type: application/json" \
      -d '{
        "username": "testuser",
        "password": "testpassword",
        "}

  **Obtener el Token de acceso**:
  
    curl -X POST "http://127.0.0.1:8000/api/token/" \
    -H "Content-Type: application/json" \
    -d '{"username": "testuser", "password": "testpassword"}'
    
  - Respuesta JSON:

        "access": "tu_token_de_acceso",
        "refresh": "tu_token_de_refresco"



  **Crear una tarea**:
  
    curl -X POST http://127.0.0.1:8000/api/tasks/create/ \
    -H "Authorization: Bearer <tu_token_de_acceso>" \
    -d '{"title": "Nueva Tarea", "description": "Descripción de la tarea", "completed": false}' \
    -H "Content-Type: application/json"
    
  - Respuesta JSON:
      
        "id": 3,
        "title": "Mi nueva tarea",
        "description": "Descripción de mi nueva tarea",
        "completed": false


  **Listar tareas**:
  
    curl -X GET http://127.0.0.1:8000/tasks/ \
      -H "Authorization: Bearer  <tu_token_de_acceso>"

  - Respuesta JSON:
      
        "id": 1,
        "title": "Tarea listadas",
        "description": "Mis tareas",
        "completed": false





  **Actualizar una tarea existente**:
    
    curl -X PUT http://127.0.0.1:8000/tasks/1/update/ \
    -H "Authorization: Bearer <tu_token_de_acceso>" \
    -H "Content-Type: application/json" \
    -d '{"title": "Tarea 1 actualizada", "completed": true}'

    
  - Respuesta JSON:
   
        "id": 1,
        "title": "Tarea 1 actualizada",
        "description": "Descripción de la tarea 1",
        "completed": true
    

  **Eliminar una tarea existente**:
  
    curl -X DELETE http://127.0.0.1:8000/tasks/1/delete/ \
      -H "Authorization: Bearer <tu_token_de_acceso>"

    
  - Respuesta JSON:

        "message": "Tarea eliminada"











