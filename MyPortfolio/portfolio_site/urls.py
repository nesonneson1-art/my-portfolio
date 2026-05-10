from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve  # இதைப் புதுசா சேர்க்கிறோம்
from django.urls import re_path        # இதையும் சேர்க்கிறோம்

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]

# இது ஆன்லைன்ல போட்டோக்கள் தெரிய உதவும் "Power" வரிகள்
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]