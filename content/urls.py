from django.urls import path
from . import views

urlpatterns = [
	path('', views.projects_list_view, name='projects_list'),
	path('experience/', views.expereince_list_view, name='experience_list'),
]