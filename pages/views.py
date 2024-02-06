from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "pages/home.html",{})

def about(request):
    return render(request, "pages/about.html",{})

def projects_page(request):
    return render (request, "projects/projects_index.html",{})

def contact(request):
    return render(request, 'contact.html')