from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, TaskSerializer
from .models import Task

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi




# Vista para registrar un nuevo usuario
class RegisterUserAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Registra un nuevo usuario",
        request_body=UserSerializer,
        responses={201: UserSerializer, 400: "Error en los datos del usuario"}
    )

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        # Verificar si ya existe un usuario con el mismo nombre
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)

        # Generar token JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


class ObtainTokenAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Obtiene el token JWT para un usuario autenticado",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: "Token generado", 400: "Credenciales inválidas"}
    )

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)




class UserProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios autenticados

    
    @swagger_auto_schema(
        operation_description="Obtiene el perfil del usuario autenticado",
        responses={200: UserSerializer}
    )


    def get(self, request):
        user = request.user  # El usuario autenticado
        serializer = UserSerializer(user)
        return Response(serializer.data)




class TaskListAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios autenticados

    @swagger_auto_schema(
        operation_description="Obtiene la lista de tareas del usuario autenticado",
        responses={
            200: TaskSerializer(many=True),
            401: "No autorizado (usuario no autenticado)"
        }
    )

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)  # Filtrar tareas del usuario autenticado
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios autenticados

    @swagger_auto_schema(
        operation_description="Crea una nueva tarea asociada al usuario autenticado",
        request_body=TaskSerializer,
        responses={
            201: TaskSerializer,
            400: "Error en los datos de la tarea",
            401: "No autorizado (usuario no autenticado)"
        }
    )


    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # Asociamos la tarea al usuario autenticado
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios autenticados

    @swagger_auto_schema(
        operation_description="Actualiza los detalles de una tarea específica del usuario autenticado",
        request_body=TaskSerializer,
        responses={
            200: TaskSerializer,
            400: "Error en los datos de la tarea",
            404: "Tarea no encontrada",
            401: "No autorizado (usuario no autenticado)"
        }
    )

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Filtra solo tareas del usuario autenticado
        except Task.DoesNotExist:
            return Response({"error": "Tarea no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios autenticados

    @swagger_auto_schema(
        operation_description="Elimina una tarea específica del usuario autenticado",
        responses={
            204: "Tarea eliminada",
            404: "Tarea no encontrada",
            403: "No autorizado (el usuario no tiene permiso para eliminar esta tarea)",
            401: "No autorizado (usuario no autenticado)"
        }
    )

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Filtra solo tareas del usuario autenticado
        except Task.DoesNotExist:
            return Response({"error": "Tarea no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"message": "Tarea eliminada"}, status=status.HTTP_204_NO_CONTENT)

class TaskFilterAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Solo accesible para usuarios autenticados

    
    @swagger_auto_schema(
        operation_description="Filtra las tareas del usuario autenticado por estado (completada o no)",
        manual_parameters=[
            openapi.Parameter(
                'completed', openapi.IN_QUERY, description="Filtrar tareas por estado de completado (true/false)",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: TaskSerializer(many=True),
            401: "No autorizado (usuario no autenticado)"
        }
    )

    def get(self, request):
        completed = request.query_params.get('completed', None)
        tasks = Task.objects.filter(user=request.user)  # Filtra tareas del usuario autenticado

        if completed is not None:
            tasks = tasks.filter(completed=completed.lower() == 'true')  # Filtra por estado completado

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


