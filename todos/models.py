from django.db import models
from config.settings import base
from config import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(settings.base.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Todo(models.Model):
    todo_job = models.CharField(max_length=200)
    todo_job_detail = models.TextField(default='Todo detail')
    # user = models.ForeignKey('Person', on_delete=True)
    user = models.ForeignKey(settings.base.AUTH_USER_MODEL)
    category = models.ForeignKey('Category')
    is_finished = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.todo_job


