from django.contrib import admin

# Register your models here.

from .models import Todo, Category


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    fields = (('todo_job', 'user', 'is_finished'), 'category', 'todo_job_detail',)
    list_display = ('todo_job', 'todo_job_detail', 'category', 'is_finished', 'user',)
    list_filter = ('user', 'is_finished', 'category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass




