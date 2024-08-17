from django.shortcuts import render
from projects.models import Project


def list_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/ProjectsList.html', {'projects': projects})
