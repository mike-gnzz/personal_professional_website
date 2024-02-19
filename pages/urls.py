from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', include('projects.urls')),
    path('contributions/', include('contributions.urls'))

]