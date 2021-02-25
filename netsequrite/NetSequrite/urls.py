from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


apipatterns = [
    path('v1/', include('patrimoine.api.v1.urls')),
    path('v1/', include('cases.api.v1.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, 'api'), namespace='api')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)