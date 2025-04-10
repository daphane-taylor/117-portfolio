from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_list_view(request):
	projects = Project.objects.all()
	return render(request, 'content/projects_list.html',('projects': projects))

def expereince_list_view(request):
	return render(request, 'content/experience_list.html')