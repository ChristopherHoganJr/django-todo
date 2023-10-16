from django.shortcuts import render

# Models
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False)
    print(tasks)
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)