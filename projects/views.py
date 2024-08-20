from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/ProjectsList.html', {'projects': projects})


@login_required
def show_project(request, id):
    detail = Project.objects.get(id=id)
    return render(request, 'projects/DetailProject.html', {'detail': detail })
