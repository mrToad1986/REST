from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=128)
    ref = models.URLField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class TODO(models.Model):
    project = models.ForeignKey(User, related_name='_project', on_delete=models.PROTECT)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='_user', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project
