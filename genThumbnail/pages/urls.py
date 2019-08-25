from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homePageView, generateThumbnailView, generateThumbnailAsync

urlpatterns = [
    path('', homePageView, name='home'),
    path('generateThumbnail', generateThumbnailView,
         name='generateThumbnail'),
    path('generateThumbnailAsync', generateThumbnailAsync,
         name='generateThumbnailAsync')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
