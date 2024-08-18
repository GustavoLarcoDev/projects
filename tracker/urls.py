from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_list_projects(request):
    return redirect("list_projects")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("", redirect_to_list_projects, name="home"),
    path("accounts/", include('accounts.urls')),
]
