from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path("contact/", include("contact.urls")),
    path("bag/", include("bag.urls")),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('comments/', include('comments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)