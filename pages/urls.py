from django.urls import path
from . import views
from .views import project_list

urlpatterns = [
    path('', views.about_view, name='about'),
path('projects/', views.project_list, name='project_list'),
path('contact/', views.contact_view, name='contact'),
]

