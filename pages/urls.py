from django.urls import path, include
from pages import views

urlpatterns = [
    path('michaelgnzz.me', views.home, name='home'),
    path('projects/', include('projects.urls')),

]