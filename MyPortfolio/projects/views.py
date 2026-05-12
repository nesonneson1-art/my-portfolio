from django.shortcuts import render, redirect
from .models import Project, Profile, Contact # Contact மாடலையும் சேர்த்துக்கோங்க

def project_index(request):
    # --- 1. மெசேஜைச் சேமிக்கும் பகுதி ---
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # டேட்டாபேஸ்ல சேமிக்கிறோம்
        Contact.objects.create(name=name, email=email, message=message)
        
        # சேமிச்சதுக்கு அப்புறம் அதே பேஜுக்கு ரீடைரக்ட் பண்றோம்
        return redirect('project_index')

    # --- 2. தகவல்களைக் காட்டும் பகுதி ---
    projects = Project.objects.all()
    profile = Profile.objects.first() 
    context = {
        'projects': projects,
        'profile': profile,
    }
    return render(request, 'project_index.html', context)