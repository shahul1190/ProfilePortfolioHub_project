from .forms import  ProjectForm
from .models import Project
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Profile




def home_view(request):
    return render(request, 'home.html')

def indextwo(request):
    return render(request,'index.html')

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user.profile
            project.save()
            return redirect('project_detail')
    else:
        form = ProjectForm()
    return render(request, 'project_create.html', {'form': form})
@login_required
def project_edit(request):
    project = Project.objects.filter(profile=request.user.profile).last()
    if project is None:
        return redirect('project_create')
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_edit.html', {'form': form})

@login_required
def project_detail(request):
    project = Project.objects.filter(profile=request.user.profile).last()
    if project is None:
        return redirect('project_create')
    return render(request, 'port.html', {'project': project})


@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('create_profile')
    return render(request, 'user_profile.html', {'profile': profile})


@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})






























