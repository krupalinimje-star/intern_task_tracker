from rest_framework import serializers
from django.utils import timezone
# pyrefly: ignore [missing-import]
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority', 
            'due_date', 'created_at', 'updated_at', 'owner'
        ]

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("The due date cannot be in the past.")
        return value
