from django.shortcuts import render
from projects.models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, "pages/home.html",{'projects':projects})

def about(request):
    return render(request, "pages/about.html",{})

def projects_page(request):
    return render (request, "projects/projects_index.html",{})

def contact(request):
    return render(request, 'contact.html')