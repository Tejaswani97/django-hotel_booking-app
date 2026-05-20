from django.contrib import admin
from django.urls import path, include
from hotels import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('', include('hotels.urls')),
]

# ✅ ADD THIS (VERY IMPORTANT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
