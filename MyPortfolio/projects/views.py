# from django.shortcuts import render, redirect
# from .models import Project, Profile, Contact # Contact மாடலையும் சேர்த்துக்கோங்க

# def project_index(request):
#     # --- 1. மெசேஜைச் சேமிக்கும் பகுதி ---
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         # டேட்டாபேஸ்ல சேமிக்கிறோம்
#         Contact.objects.create(name=name, email=email, message=message)
        
#         # சேமிச்சதுக்கு அப்புறம் அதே பேஜுக்கு ரீடைரக்ட் பண்றோம்
#         return redirect('project_index')

#     # --- 2. தகவல்களைக் காட்டும் பகுதி ---
#     projects = Project.objects.all()
#     profile = Profile.objects.first() 
#     context = {
#         'projects': projects,
#         'profile': profile,
#     }
#     return render(request, 'project_index.html', {'profile': profile})
#     return render(request, 'project_index.html', {'projects': projects})

def project_index(request):
    # --- 1. மெசேஜைச் சேமிக்கும் பகுதி (இது சரியா இருக்கு) ---
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('project_index')

    # --- 2. தகவல்களைக் காட்டும் பகுதி ---
    projects = Project.objects.all()
    profile = Profile.objects.first() 
    
    # எல்லா தகவல்களையும் ஒரே Context-க்குள் போடுங்க
    context = {
        'projects': projects,
'profile': profile if profile else {}, # டேட்டா இல்லைனா காலியா அனுப்பும்
    }
    
    # ஒரே ஒரு ரிட்டர்ன் மட்டுமே இருக்கணும்!
    return render(request, 'project_index.html', context)