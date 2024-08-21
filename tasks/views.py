from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": TaskForm
    }

    return render(request, "tasks/CreateTask.html", context)


@login_required
def show_my_task(request):
    context = {
        "tasks": Task.objects.filter(assignee=request.user),
    }
    return render(request, "tasks/Task.html", context)
