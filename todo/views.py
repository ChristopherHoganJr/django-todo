from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('/')

# Mark a task as completed
def markAsCompleted(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('/')

# Mark a task as incompleted
def markAsIncompleted(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('/')

# Edit a task
def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('/')
    else:
        context = {
            'task': task
        }
        return render(request, 'editTask.html', context)

# Delete a task
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/')
