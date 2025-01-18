from django.urls import path
from .views import TaskListAPIView, TaskCreateAPIView, TaskUpdateAPIView, TaskDeleteAPIView, RegisterUserAPIView, UserProfileAPIView, ObtainTokenAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),  # Registrar usuario
    path('token/', ObtainTokenAPIView.as_view(), name='get-token'),  # Obtener token
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),  # Ver perfil del usuario
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),  # Listar tareas
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),  # Crear tarea
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task-update'),  # Actualizar tarea
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='task-delete'),  # Eliminar tarea
]
