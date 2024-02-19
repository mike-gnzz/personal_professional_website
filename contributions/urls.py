from django.urls import path
from contributions import views

urlpatterns = [
    path("<int:pk>/", views.contribution_detail, name='contribution_detail'),
]
