from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django_email_verification import urls as email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('models.urls')),
    path('auth/', include('AUTH.urls')),
    path('email/', include(email_urls), name='email-verification'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)