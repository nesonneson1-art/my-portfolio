# # # from django.contrib import admin
# # # from .models import Project, Contact, Profile # Profile-ஐ இங்கே சேர்க்கவும்

# # # admin.site.register(Project)
# # # admin.site.register(Contact)
# # # admin.site.register(Profile) # இதையும் இங்கே சேர்க்கவும்
# # from django.contrib import admin
# # from django.utils.html import format_html # இதை மறக்காம சேருங்க
# # from .models import Project, Profile

# # class ProjectAdmin(admin.ModelAdmin):
# #     # இது அட்மின் லிஸ்ட்ல படத்தைக் காட்டும்
# #     def image_preview(self, obj):
# #         if obj.image:
# #             return format_html('<img src="{}" style="width: 100px; height: auto; border-radius: 5px;" />', obj.image.url)
# #         return "No Image"

# #     readonly_fields = ['image_preview'] # எடிட் பண்ணும்போது படத்தைக் காட்டும்
# #     list_display = ['title', 'image_preview'] # லிஸ்ட்ல படத்தைக் காட்டும்

# # class ProfileAdmin(admin.ModelAdmin):
# #     def profile_preview(self, obj):
# #         if obj.image:
# #             return format_html('<img src="{}" style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover;" />', obj.image.url)
# #         return "No Image"

# #     readonly_fields = ['profile_preview']
# #     list_display = ['name', 'profile_preview']
# # class Media:
# #         css = {
# #             'all': ('css/admin_custom.css',)
# #         }

# # # மாடல்களை ரிஜிஸ்டர் செய்யும் முறை
# # admin.site.register(Project, ProjectAdmin)
# # admin.site.register(Profile, ProfileAdmin)
# # from django.contrib import admin
# # from django.utils.html import format_html
# # from .models import Project, Profile, Contact

# # class ProfileAdmin(admin.ModelAdmin):
# #     # இங்க தான் நீங்க போட்டோவோட அளவை (150px) மாத்தி அட்ஜஸ்ட் பண்ண முடியும்
# #     def photo_preview(self, obj):
# #         if obj.image:
# #             return format_html('<img src="{}" style="width:150px; height:150px; object-fit:cover; border-radius:10px; border: 2px solid #ddd;" />', obj.image.url)
# #         return "No Photo"

# #     readonly_fields = ['photo_preview']
# #     list_display = ['name', 'photo_preview'] # லிஸ்ட்ல பாக்குறதுக்கு
# #     fields = ['name', 'image', 'photo_preview', 'bio'] # எடிட் பண்ணும்போது பாக்குறதுக்கு

# # class ProjectAdmin(admin.ModelAdmin):
# #     def project_photo(self, obj):
# #         if obj.image:
# #             return format_html('<img src="{}" style="width:200px; height:auto; border-radius:5px;" />', obj.image.url)
# #         return "No Image"

# #     readonly_fields = ['project_photo']
# #     list_display = ['title', 'project_photo']
# #     fields = ['title', 'description', 'technology', 'image', 'project_photo', 'link']

# # # இதோ இந்த வரிகள் மட்டும் இருந்தாலே போதும்
# # admin.site.register(Profile, ProfileAdmin)
# # admin.site.register(Project, ProjectAdmin)
# # admin.site.register(Contact)
# # from django.contrib import admin
# # from django.utils.html import format_html
# # from .models import Project, Profile, Contact
# # from image_cropping import ImageCroppingMixin

# # class ProfileAdmin(admin.ModelAdmin):
# #     # இங்க தான் 'profile_pic' அப்படின்னு மாத்தி இருக்கேன்
# #     def photo_preview(self, obj):
# #         if obj.profile_pic:
# #             return format_html('<img src="{}" style="width:150px; height:150px; object-fit:cover; border-radius:10px;" />', obj.profile_pic.url)
# #         return "No Photo"

# #     readonly_fields = ['photo_preview']
# #     list_display = ['name', 'photo_preview']
# #     # 'image' என்ற இடத்தை 'profile_pic' என்று மாத்திட்டேன்
# #     fields = ['name', 'profile_pic', 'photo_preview', 'email', 'phone', 'location', 'about_me', 'portfolio_title', 'sub_title', 'linkedin', 'github', 'resume']

# # class ProjectAdmin(admin.ModelAdmin):
# #     def project_photo(self, obj):
# #         if obj.image:
# #             return format_html('<img src="{}" style="width:200px; height:auto; border-radius:5px;" />', obj.image.url)
# #         return "No Image"


# # class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
# #     pass

# #     readonly_fields = ['project_photo']
# #     list_display = ['title', 'project_photo']
# #     # இங்க 'github_link' என்று மாடல்ல இருக்கிற மாதிரியே கொடுத்திருக்கேன்
# #     fields = ['title', 'description', 'technology', 'image', 'project_photo', 'github_link']

# # # பழைய ரிஜிஸ்டர் வரிகள் இருந்தா நீக்கிட்டு இதை மட்டும் வைங்க
# # admin.site.register(Profile, ProfileAdmin)
# # admin.site.register(Project, ProjectAdmin)
# # admin.site.register(Contact)
# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Project, Profile, Contact
# from image_cropping import ImageCroppingMixin # மவுஸ் அட்ஜஸ்ட்மென்ட்க்கு இது முக்கியம்

# # 1. ப்ரொபைல் அட்ஜஸ்ட்மென்ட் (மவுஸ் மூலம் Crop செய்ய)
# class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
#     def photo_preview(self, obj):
#         if obj.profile_pic:
#             return format_html('<img src="{}" style="width:150px; height:150px; object-fit:cover; border-radius:10px;" />', obj.profile_pic.url)
#         return "No Photo"

#     readonly_fields = ['photo_preview']
#     list_display = ['name', 'photo_preview']
#     # 'cropping' ஃபீல்டு தான் அந்த மவுஸ் பாக்ஸைக் கொண்டு வரும்
#     fields = ['name', 'profile_pic', 'cropping', 'photo_preview', 'email', 'phone', 'location', 'about_me', 'portfolio_title', 'sub_title', 'linkedin', 'github', 'resume']

# # 2. ப்ராஜெக்ட் அட்ஜஸ்ட்மென்ட்
# class ProjectAdmin(admin.ModelAdmin):
#     def project_photo(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" style="width:200px; height:auto; border-radius:5px;" />', obj.image.url)
#         return "No Image"

#     readonly_fields = ['project_photo']
#     list_display = ['title', 'project_photo']
#     fields = ['title', 'description', 'technology', 'image', 'project_photo', 'github_link']

# # மாடல்களை ரிஜிஸ்டர் செய்தல்
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Project, ProjectAdmin)
# admin.site.register(Contact)

    
from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Profile, Contact


# # 1. Profile Admin Settings
# class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
#     def photo_preview(self, obj):
#         if obj.profile_pic:
#             return format_html('<img src="{}" style="width:100px; height:100px; object-fit:cover; border-radius:10px;" />', obj.profile_pic.url)
#         return "No Photo"

#     readonly_fields = ['photo_preview']
#     list_display = ['name', 'photo_preview']
#     fields = [
#         'name', 'profile_pic', 'cropping', 'photo_preview', 
#         'email', 'phone', 'location', 'about_me', 
#         'portfolio_title', 'sub_title', 'linkedin', 'github', 'resume'
#     ]

from django.contrib import admin
from django.utils.html import format_html
# Project மற்றும் Contact மாடல்களையும் இங்கே Import செய்ய வேண்டும்
from .models import Profile, Project, Contact 

# 1. Profile Admin Settings
class ProfileAdmin(admin.ModelAdmin):
    def photo_preview(self, obj):
        if obj.profile_pic:
            return format_html('<img src="{}" style="width:100px; height:100px; object-fit:cover; border-radius:10px;" />', obj.profile_pic.url)
        return "No Photo"

    photo_preview.short_description = 'Preview'
    readonly_fields = ['photo_preview']
    list_display = ['name', 'photo_preview']
    fields = [
        'name', 'profile_pic', 'photo_preview', 
        'email', 'phone', 'location', 'about_me', 
        'portfolio_title', 'sub_title', 'linkedin', 'github', 'resume'
    ]

# 2. Project Admin Settings
class ProjectAdmin(admin.ModelAdmin):
    def project_photo(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:200px; height:auto; border-radius:5px;" />', obj.image.url)
        return "No Image"

    readonly_fields = ['project_photo']
    list_display = ['title', 'project_photo']
    fields = ['title', 'description', 'technology', 'image', 'project_photo', 'github_link']

# 3. Model Registration (ஒவ்வொன்றும் ஒரு முறை மட்டுமே இருக்க வேண்டும்)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact)