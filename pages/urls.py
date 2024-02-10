from django.urls import path, include
from pages import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('projects/', include('projects.urls')),

]