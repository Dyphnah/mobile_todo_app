from rest_framework.serializers import ModelSerializer
from .models import Comment, Project, Task

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

