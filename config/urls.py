from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace="pages"), ),
    path('listings/', include('listings.urls', namespace="listings"), ),
    path('realtors/', include('realtors.urls', namespace="realtors"), ),
    path('accounts/', include('accounts.urls', namespace="accounts"), ),
    path('contacts/', include('contacts.urls', namespace="contacts"), )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)