"""
URL configuration for Takhlees Business project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

def health_check(request):
    """
    Health check endpoint returning system status and configuration indicators.
    """
    return JsonResponse({
        "status": "healthy",
        "service": "takhlees-backend-api",
        "version": "1.0.0",
        "environment": "development" if settings.DEBUG else "production",
        "database": settings.DATABASES['default']['ENGINE'].split('.')[-1],
        "regions": ["ae", "in"],
    })

# API v1 URL patterns
api_v1_patterns = [
    path('health/', health_check, name='health-check'),
    # Apps will mount their endpoints here as features are developed:
    # path('accounts/', include('apps.accounts.urls')),
    # path('courses/', include('apps.courses.urls')),
    # path('services/', include('apps.services.urls')),
    # path('branches/', include('apps.branches.urls')),
    # path('admissions/', include('apps.admissions.urls')),
    # path('enquiries/', include('apps.enquiries.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include((api_v1_patterns, 'v1'))),
    # OpenAPI Schema & Interactive Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Direct Root Health Check
    path('health/', health_check, name='root-health-check'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
