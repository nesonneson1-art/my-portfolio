from django.shortcuts import render
from .models import Project, Profile # Profile-ஐயும் இங்கே சேர்க்கவும்

def project_index(request):
    projects = Project.objects.all()
    profile = Profile.objects.first() # அட்மினில் சேர்த்த முதல் ப்ரொபைலை எடுக்கும்
    context = {
        'projects': projects,
        'profile': profile
    }
    return render(request, 'project_index.html', context)