



from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()

    return render(request, "main/index.html", {
        "projects": projects
    })