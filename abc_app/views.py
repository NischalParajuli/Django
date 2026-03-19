from django.shortcuts import render, redirect
from .models import Todolist


def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def todolist(request):
    tasks = Todolist.objects.all().order_by("id")
    completed = Todolist.objects.filter(status=True).count()
    incomplete = Todolist.objects.filter(status=False).count()

    context = {
        "tasks": tasks,
        "complete": completed,
        "incomplete": incomplete,
    }
    return render(request, 'list.html', context)


def create(request):
    if request.method == "POST":
        user_title = request.POST.get('title', '').strip()
        user_description = request.POST.get('description', '').strip()

        if not user_title or not user_description:
            context = {"error": "Both fields are required"}
            return render(request, 'create.html', context)

        Todolist.objects.create(title=user_title, description=user_description)
        return redirect('task-list')

    return render(request, 'create.html')


def delete(request, id):
    task = Todolist.objects.get(id=id)
    task.delete()
    return redirect('task-list')


def toggle(request, id):
    task = Todolist.objects.get(id=id)
    task.status = not task.status
    task.save()
    return redirect('task-list')