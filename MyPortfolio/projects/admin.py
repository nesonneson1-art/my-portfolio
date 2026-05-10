from django.contrib import admin
from .models import Project, Contact, Profile # Profile-ஐ இங்கே சேர்க்கவும்

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Profile) # இதையும் இங்கே சேர்க்கவும்