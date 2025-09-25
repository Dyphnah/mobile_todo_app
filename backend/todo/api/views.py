from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Project, Task, Comment
from .seriallizers import ProjectSerializer, TaskSerializer, CommentSerializer

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'add_task':
            return TaskSerializer
        if self.action == 'add_comment':
            return CommentSerializer
        return ProjectSerializer

    def create(self, request):
        user = request.user
        if not user.is_staff and not getattr(user, 'role', None) in ['manager', 'owner']:
            return Response({'detail': 'You do not have permission to create a project.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        project = self.get_object()
        comments = Comment.objects.filter(project=project)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        project = self.get_object()
        data = request.data.copy()
        data['project'] = project.id
        data['written_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        project = self.get_object()
        tasks = Task.objects.filter(project=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_task(self, request, pk=None):
        project = self.get_object()
        data = request.data.copy()
        data['project'] = project.id
        data['assigned_to'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def completed(self, request, pk=None):
        task = self.get_object()
        task.status = 'completed'
        task.save()
        return Response({'status': 'Task marked as completed'})

    @action(detail=True, methods=['post'])
    def pending(self, request, pk=None):
        task = self.get_object()
        task.status = 'pending'
        task.save()
        return Response({'status': 'Task marked as pending'})

    @action(detail=True, methods=['post'])
    def review(self, request, pk=None):
        task = self.get_object()
        task.status = 'review'
        task.save()
        return Response({'status': 'Task marked for review'})

    @action(detail=True, methods=['post'])
    def in_progress(self, request, pk=None):
        task = self.get_object()
        task.status = 'in_progress'
        task.save()
        return Response({'status': 'Task marked as in progress'})

    @action(detail=True, methods=['post'])
    def backlog(self, request, pk=None):
        task = self.get_object()
        task.status = 'blocked'
        task.save()
        return Response({'status': 'Task marked as blocked'})

class CommentView(viewsets.ModelViewSet):
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
