from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from django.utils import timezone
from .models import Folder
from .models import Task
from .serializers import FolderSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q

"""
ViewSet for managing Folder model instances.
"""
class FolderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    """
    Overrides the default queryset to only return folders assigned to the current user.
    """
    def get_queryset(self):
        queryset = Folder.objects.all()
        user = self.request.user

        return queryset.filter(assigned_to=user)

"""
ViewSet for managing Task model instances.
"""
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (OrderingFilter, )
    ordering_fields = ('title', 'priority', 'deadline')
    pagination_class = LimitOffsetPagination

    """
    Overrides the default queryset to filter tasks based on various query parameters.
    """
    def get_queryset(self):
        queryset = Task.objects.all()
        user = self.request.user
        search_param = self.request.query_params.get('search')
        completed_param = self.request.query_params.get('completed')
        status_param = self.request.query_params.get('status')
        folder_param = self.request.query_params.get('folder_id')

        if search_param:
            queryset = queryset.filter(Q(title__icontains=search_param) | Q(description__icontains=search_param))
        
        if completed_param in ['true', 'false']:
            completed = completed_param == 'true'
            queryset = queryset.filter(completed=completed)

        if status_param:
            if status_param == 'overdue':
                queryset = queryset.filter(deadline__lt=timezone.now())
            elif status_param == 'upcoming':
                queryset = queryset.filter(deadline__gte=timezone.now())
        
        if folder_param:
            queryset = queryset.filter(folder_id=folder_param)

        return queryset.filter(assigned_to=user)

"""
API view for marking a task as completed or uncompleted.
"""
class CompleteTask(APIView):
    def put(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.completed = not task.completed
            task.save()
            return Response({'message': 'Task status updated'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'message': 'The task does not exist'}, status=status.HTTP_404_NOT_FOUND)