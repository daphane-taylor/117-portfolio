from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
def projects_list_view(request):
	projects = Project.objects.all().order_by('-year')

	return render(request, 'content/projects_list.html', {'projects': projects})

@login_required
def project_delete(request, pk):
	project = get_object_or_404(Project, pk=pk)

	if request.method == 'POST':
		project.delete()
		return redirect('projects_list')
	return render(request, 'content/project_delete_confirmation.html', {'project': project})

@login_required
def project_new_view(request):
    form = ProjectForm()
    return render(request, "content/project_new.html", {'form': form})

@login_required
def project_update_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'content/project_update.html', {'form': form, 'project': project})

def experience_list_view(request):
	return render(request, 'content/experience_list.html')