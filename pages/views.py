from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "pages/home.html",{})

def other_page(request):
    return render(request, "pages/other_page.html",{})

def projects_page(request):
    return render (request, "projects/project_index.html",{})