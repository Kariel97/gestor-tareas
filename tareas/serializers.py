from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from .models import Task

# Serializador para el modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user']

        

# Serializador para el modelo Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'completed']
        
    title = serializers.CharField(
        validators=[MinLengthValidator(3, message="El título debe tener al menos 3 caracteres.")]
    )
