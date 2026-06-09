from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
# pyrefly: ignore [missing-import]
from.models import Task
# pyrefly: ignore [missing-import]
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    # 1. Enforce authentication
    permission_classes = [permissions.IsAuthenticated]

    # 2. Add standard filtering and search backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # 3. Specify standard filters for status and priority
    filterset_fields = ['status', 'priority']
    
    # 4. Enable title searching
    search_fields = ['title']

    # 5. Overdue logic + owner isolation in get_queryset
    def get_queryset(self):
        # Start by fetching tasks belonging only to the logged-in user
        queryset = Task.objects.filter(owner=self.request.user)

        # Check if the user requested to see only overdue tasks (?overdue=true)
        overdue = self.request.query_params.get('overdue', None)
        if overdue == 'true':
            today = timezone.now().date()
            # An overdue task is one where the due date is in the past
            # and the task is NOT Completed (i.e. is Pending or In Progress)
            queryset = queryset.filter(due_date__lt=today).exclude(status='Completed')

        return queryset

    # 6. Set the task owner dynamically on creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

