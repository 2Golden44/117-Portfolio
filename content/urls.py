from django.urls import path
from content import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.project_list_view, name='project_list'),
    path('add/', views.add_project_view, name='add'),
     path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]