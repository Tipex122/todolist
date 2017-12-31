from django import forms

from .models import Todo, Category


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('todo_job', 'todo_job_detail', 'category', 'is_finished', 'user')  # 'created_date')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
