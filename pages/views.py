from django.shortcuts import render
from projects.models import Project
from contributions.models import Contributions
from personal_portfolio.settings import STATIC_URL
# Create your views here.

def home(request):
    email = "gnzz.michael@gmail.com"
    location = "California"
    LinkedIn_url = 'https://www.linkedin.com/in/michael-gonzalez-69935a178/'
    resume_url = STATIC_URL / 'pages/PDF/Michael_Gonzalez_CV.pdf'
    projects = Project.objects.all()
    contributions = Contributions.objects.all()
    return render(request, "pages/home.html",{'projects':projects,
                                              'contributions':contributions,
                                              'email':email,
                                              'location': location,
                                              "LinkedIn_url": LinkedIn_url,
                                              'resume_url': resume_url})

