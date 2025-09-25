from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('staff', 'Staff'),
        ('project_manager', 'Project Manager'),
        ('client', 'Client'),
        ('owner', 'Owner'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return f"{self.username} ({self.role})"


class Project(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]

    project_name = models.CharField(max_length=30)
    project_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_projects')


    def __str__(self):
        return self.project_name


class Task(models.Model):
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('review', 'Review'),
    ('completed', 'Completed'),
    ('blocked', 'Blocked'),
]

    title = models.CharField(max_length=30)
    description = models.TextField()
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subtasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    depends_on = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='dependent_tasks')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to =models.ForeignKey( User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        db_table ='Tasks'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    title =models.CharField (max_length= 30)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    written_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table ='Comments'

    def __str__(self):
        return self.title

