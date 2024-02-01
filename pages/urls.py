from django.urls import path
from pages import views
from projects import views as pv
urlpatterns = [
    path("", views.home, name='home'),
    path('resume/', views.other_page, name='resume'),
    path("projects/", pv.project_index, name='projects'),
]