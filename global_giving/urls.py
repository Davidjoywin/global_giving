from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("geeve.urls", namespace="geeve")),
    path('auth/', include("geeve_auth.urls", namespace="auth")),
    path('__reload__/', include('django_browser_reload.urls')),
]
