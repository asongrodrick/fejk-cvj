from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/projects/', views.api_projects, name='api_projects'),
    path('contact/', views.contact, name='contact'),
]
