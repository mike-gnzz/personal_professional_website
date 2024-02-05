from django.urls import path
from pages import views
from projects import views as pv
urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about_me, name='about'),
    path("projects/", views.projects_page, name='projects'),
    path("contact/", views.contact, name="contact"),

]