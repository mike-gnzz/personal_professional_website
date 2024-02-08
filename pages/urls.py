from django.urls import path, include
from pages import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', include('projects.urls')),
    path('contact/', views.contact, name='contact'),

]