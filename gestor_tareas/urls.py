from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de la vista de documentación Swagger/OpenAPI
schema_view = get_schema_view(
   openapi.Info(
      title="Gestor de Tareas API",
      default_version='v1',
      description="API para gestionar tareas de usuario",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@tareas.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tareas.urls')),  # Rutas de la API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Ruta para la interfaz de Swagger
]
