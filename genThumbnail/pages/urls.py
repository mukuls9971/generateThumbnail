from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homePageView, generateThumbnailView

urlpatterns = [
    path('', homePageView, name='home'),
    path('generateThumbnail', generateThumbnailView, name='generateThumbnail')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
