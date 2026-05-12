# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve  # இதைப் புதுசா சேர்க்கிறோம்
# from django.urls import re_path        # இதையும் சேர்க்கிறோம்

# urlpatterns = [
#     path('neson/', admin.site.urls),
#     path('', include('projects.urls')),
# ]

# # இது ஆன்லைன்ல போட்டோக்கள் தெரிய உதவும் "Power" வரிகள்
# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#     re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
# ]
from django.contrib import admin
from django.urls import path, include, re_path # re_path இங்கேயே சேர்த்துக்கலாம்
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('neson/', admin.site.urls), # உங்க அட்மின் லிங்க் 'neson'னு மாத்தியிருக்கீங்க, சூப்பர்!
    path('', include('projects.urls')),
]

# மீடியா மற்றும் ஸ்டேடிக் ஃபைல்களைச் சேர்க்க
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]