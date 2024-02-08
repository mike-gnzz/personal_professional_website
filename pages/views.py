from django.shortcuts import render
from projects.models import Project

# Create your views here.

def home(request):
    email = "gnzz.michael@gmail.com"
    location = "California"
    LinkedIn_url = 'https://www.linkedin.com/in/michael-gonzalez-69935a178/'
    resume_url = '/static/pages/PDF/Michael_Gonzalez_CV.pdf'
    projects = Project.objects.all()
    return render(request, "pages/home.html",{'projects':projects,
                                              'email':email,
                                              'location': location})

def about(request):
    return render(request, "pages/about.html",{})

def project_page(request):
    return render (request, "projects/project_detail.html",{})

def contact(request):
    return render(request, 'contact.html')