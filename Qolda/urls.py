from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('static_pages.urls')),
    path('professions/', include('professions.urls')),
    path('recommendations/', include('recommendations.urls')),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('api/v1/', include('api_v1.urls')),
    path('questions/', include('questions.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
