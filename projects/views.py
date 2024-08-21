from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/ProjectsList.html', {'projects': projects})


@login_required
def show_project(request, id):
    detail = Project.objects.get(id=id)
    return render(request, 'projects/DetailProject.html', {'detail': detail })


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form
    }

    return render(request, "projects/CreateProject.html", context)
