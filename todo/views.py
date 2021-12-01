from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo.objects.create(task=task)
    return redirect('index')

def delete(request, task_id):
    task = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'delete.html', {'task': task})

def completed(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def update(request, task_id):
    task = Todo.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            task.updated = True
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'update.html', context)

