from django.shortcuts import render
from .models import Task

def taskList(request):
    tasks = Task.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
