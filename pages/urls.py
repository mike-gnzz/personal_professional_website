from django.urls import path
from pages import views
from projects import views as pv
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', pv.project_index, name='projects'),
    path('contact/', views.contact, name='contact'),

]